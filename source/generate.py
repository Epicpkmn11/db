#!/usr/bin/env python3

import datetime
from dateutil import parser
import io
import json
import numpy
import os
from PIL import Image, ImageDraw
import qrcode
import re
import requests
import rfeed
import sys
import untangle
import yaml

# No py 2
if(sys.version_info.major != 3):
	print("This is Python %d!\nPlease use Python 3!" % sys.version_info.major)
	exit()

# Convert names to lowercase alphanumeric + underscore and hyphen
def webName(name):
	name = name.lower()
	out = ""
	for letter in name:
		if letter in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
			out += letter
		elif letter == " ":
			out += "-"
	return out

def ucs2Name(string):
	return "".join(list(filter(lambda c: ord(c) < 0xFFFF, string))).strip()

# Convert names to lowercase alphanumeric + underscore and hyphen
def byteCount(bytes):
	if(type(bytes) != int):
		bytes = int(bytes)

	if bytes == 1:
		return "%d Byte" % bytes
	elif bytes < (1 << 10):
		return "%d Bytes" % bytes
	elif bytes < (1 << 20):
		return "%d KiB" % (bytes // (1 << 10))
	elif bytes < (1 << 30):
		return "%d MiB" % (bytes // (1 << 20))
	else:
		return "%d GiB" % (bytes // (1 << 30))

# Recursively formats every string in an object using f-strings, pretty dangerous
# as any code can be run, so limit to where needed
def formatAll(app, item):
	if type(item) == list:
		for i in range(len(item)):
			if type(item[i]) == str:
				item[i] = eval('f"' + item[i] + '"')
			else:
				formatAll(app, item[i])
	elif type(item) == dict:
		for a in item:
			if(type(item[a]) == str):
				item[a] = eval('f"' + item[a] + '"')
			else:
				formatAll(app, item[a])

def downloadScript(file, url):
	if file[file.rfind(".") + 1:].lower() == "3dsx":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "%3DSX%/" + file,
				"message": "Downloading " + file + "..."
			}
		]
	elif file[file.rfind(".") + 1:].lower() == "nds":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "%NDS%/" + file,
				"message": "Downloading " + file + "..."
			}
		]
	elif file[file.rfind(".") + 1:].lower() == "cia":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/" + file,
				"message": "Downloading " + file + "..."
			},
			{
				"type": "installCia",
				"file": "/" + file,
				"message": "Installing " + file + "..."
			},
			{
				"type": "deleteFile",
				"file": "sdmc:/" + file,
				"message": "Deleting " + file + "."
			}
		]
	elif file[file.rfind(".") + 1:].lower() == "firm":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/luma/payloads/" + file,
				"message": "Downloading " + file + "..."
			}
		]
	elif file[file.rfind(".") + 1:].lower() in ["zip", "7z", "rar"]:
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/" + file,
				"message": "Downloading " + file + "..."
			},
			{
				"type": "extractFile",
				"file": "sdmc:/" + file,
				"input": "",
				"output": "%ARCHIVE_DEFAULT%/" + file[0:file.find(".")] + "/",
				"message": "Extracting " + file + "..."
			},
			{
				"type": "deleteFile",
				"file": "sdmc:/" + file,
				"message": "Deleting " + file +"..."
			}
		]
	else:
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/" + file,
				"message": "Downloading " + file + "..."
			}
		]

# Read json
with open("source.json", "r", encoding="utf8") as file:
	source = json.load(file)

# Read version from old unistore
with open(os.path.join("..", "unistore", "universal-db.unistore"), "r", encoding="utf8") as file:
	unistoreOld = json.load(file)

# Create UniStore base
unistore = {
	"storeInfo": {
		"title": "Universal-DB",
		"author": "Universal-Team",
		"url": "https://db.universal-team.net/unistore/universal-db.unistore",
		"file": "universal-db.unistore",
		"sheetURL": "https://db.universal-team.net/unistore/universal-db.t3x",
		"sheet": "universal-db.t3x",
		"description": "Universal-DB - An online database of 3DS and DS homebrew",
		"version": 3,
		"revision": 0 if not "revision" in unistoreOld["storeInfo"] else unistoreOld["storeInfo"]["revision"]
	},
	"storeContent": [],
}

# Output json
output = []

# Old data json
oldData = None

with open(os.path.join("..", "data", "full.json"), "r", encoding="utf8") as file:
	oldData = json.load(file)

# Icons array
icons = []
iconIndex = 0

# Auth header
header = None
if len(sys.argv) > 1:
	header = {"Authorization": "token " + sys.argv[1]}

# Fetch info for GitHub apps and output
for app in source:
	if "github" in app:
		print("GitHub")
		api = requests.get("https://api.github.com/repos/" + app["github"], headers = header if header else None).json()
		releases = requests.get("https://api.github.com/repos/" + app["github"] + "/releases", headers = header if header else None).json()
		release = None
		prerelease = None
		if len(releases) > 0 and releases[0]["prerelease"]:
			prerelease = releases[0]
		for r in releases:
			if not r["prerelease"]:
				release = r
				break

		if not "title" in app:
			app["title"] = api["name"]

		if not "author" in app:
			app["author"] = api["owner"]["login"]

		if not "description" in app and api["description"] != "" and api["description"] != None:
			app["description"] = api["description"]

		if not "image" in app:
			app["image"] = api["owner"]["avatar_url"]

		if not "source" in app:
			app["source"] = api["html_url"]

		if not "created" in app:
			app["created"] = api["created_at"]

		if not "website" in app and api["homepage"] != "" and api["homepage"] != None:
			app["website"] = api["homepage"]

		if not "wiki" in app and api["has_wiki"]:
			app["wiki"] = api["html_url"] + "/wiki"

		if api["license"]:
			if not "license" in app:
				app["license"] = api["license"]["key"]

			if not "license_name" in app:
				app["license_name"] = api["license"]["name"]

		if release:
			if not "download_page" in app:
				app["download_page"] = release["html_url"]

			if not "version" in app:
				app["version"] = release["tag_name"]

			if not "version_title" in app and release["name"] != "" and release["name"] != None:
				app["version_title"] = release["name"]

			if not "update_notes" in app and release["body"] != "" and release["body"] != None:
				app["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": release["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

			if not "updated" in app:
				app["updated"] = release["published_at"]

			if not "downloads" in app:
				app["downloads"] = {}
			for asset in release["assets"]:
				if not asset["name"] in app["downloads"] and len(re.findall("(nro|vpk|PS3|PSP|vita|switch|wii|osx|ubuntu|win|elf)", asset["name"])) == 0:
					app["downloads"][asset["name"]] = {
						"url": asset["browser_download_url"],
						"size": asset["size"]
					}

		if prerelease:
			if not "prerelease" in app:
				app["prerelease"] = {}

			if not "download_page" in app:
				app["download_page"] = prerelease["html_url"]
			if not "download_page" in app["prerelease"]:
				app["prerelease"]["download_page"] = prerelease["html_url"]

			if not "version" in app:
				app["version"] = prerelease["tag_name"]
			if not "version" in app["prerelease"]:
				app["prerelease"]["version"] = prerelease["tag_name"]

			if not "version_title" in app and prerelease["name"] != "" and prerelease["name"] != None:
				app["version_title"] = prerelease["name"]
			if not "version_title" in app["prerelease"] and prerelease["name"] != "" and prerelease["name"] != None:
				app["prerelease"]["version_title"] = prerelease["name"]

			if not "update_notes" in app and prerelease["body"] != "" and prerelease["body"] != None:
				app["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text
			if not "update_notes" in app["prerelease"] and prerelease["body"] != "" and prerelease["body"] != None:
				app["prerelease"]["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

			if not "updated" in app:
				app["updated"] = prerelease["published_at"]
			if not "updated" in app["prerelease"]:
				app["prerelease"]["updated"] = prerelease["published_at"]

			if not "downloads" in app["prerelease"]:
				app["prerelease"]["downloads"] = {}
			for asset in prerelease["assets"]:
				if not asset["name"] in app["prerelease"]["downloads"]:
					app["prerelease"]["downloads"][asset["name"]] = {
						"url": asset["browser_download_url"],
						"size": asset["size"]
					}

	if "bitbucket" in app:
		print("Bitbucket")
		api = requests.get("https://api.bitbucket.org/2.0/repositories/" + app["bitbucket"]["repo"]).json()

		if not "title" in app:
			app["title"] = api["name"]

		if not "author" in app:
			app["author"] = api["owner"]["display_name"]

		if not "description" in app:
			app["description"] = api["description"].replace("\r\n", "\n")

		if not "image" in app:
			app["image"] = api["links"]["avatar"]["href"]

		if not "source" in app:
			app["source"] = api["links"]["html"]["href"]

		if not "created" in app:
			app["created"] = api["created_on"]

		if not "downloads" in app:
			app["downloads"] = {}
		for download in app["bitbucket"]["files"]:
			fileAPI = requests.get("https://api.bitbucket.org/2.0/repositories/" + app["bitbucket"]["repo"] + "/src/master/" + download + "?format=meta").json()
			if not download in app["downloads"]:
				app["downloads"][download] = {
					"url": fileAPI["links"]["self"]["href"],
					"size": fileAPI["size"]
				}

			if not "download_page" in app:
				app["download_page"] = "https://bitbucket.org/" + app["bitbucket"]["repo"] +"/src/master/" + download

			if not "version" in app:
				app["version"] = fileAPI["commit"]["hash"][:7]

			if not "updated" in app:
				commit = requests.get(fileAPI["commit"]["links"]["self"]["href"]).json()
				app["updated"] = commit["date"]

	# Process format strings
	if "format_strings" in app and app["format_strings"]:
		formatAll(app, app)


	if os.path.exists(os.path.join("..", "assets", "images", "screenshots", webName(app["title"]))):
		if not "screenshots" in app:
			app["screenshots"] = []
		dirlist = os.listdir(os.path.join("..", "assets", "images", "screenshots", webName(app["title"])))
		dirlist.sort()
		for screenshot in dirlist:
			if screenshot[-3:] in ["png", "gif", "jpg", "peg", "iff", "bmp"]:
				app["screenshots"].append({
					"url": "https://db.universal-team.net/assets/images/screenshots/" + webName(app["title"]) + "/" + screenshot,
					"description": screenshot[:screenshot.rfind(".")].capitalize().replace("-", " ")
				})


	if "title" in app:
		print(webName(app["title"]))
	print("=" * 80)

	# Make icon for UniStore and QR
	img = None
	if "icon" in app or "image" in app:
		if not os.path.exists("temp"):
			os.mkdir("temp")

		if "icon" in app:
			r = requests.get(app["icon"])
		else:
			r = requests.get(app["image"])

		with Image.open(io.BytesIO(r.content)) as img:
			if img.mode == "P":
				pal = img.palette.getdata()[1]
				img = img.convert("RGBA")
				data = numpy.array(img)
				r, g, b, a = data.T
				transparent = (r == pal[2]) & (g == pal[1]) & (b == pal[0])
				data[...][transparent.T] = (0, 0, 0, 0)
				img = Image.fromarray(data)
			elif img.mode != "RGBA":
				img = img.convert("RGBA")
			img.thumbnail((48, 48))
			img.save(os.path.join("temp", str(iconIndex) + ".png"))
			icons.append(str(iconIndex) + ".png")
			iconIndex += 1
			if not "color" in app:
				color = img.copy()
				color.thumbnail((1, 1))
				color = color.getpixel((0, 0))
				app["color"] = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

	# Output website page
	if "downloads" in app:
		for item in app["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["downloads"][item]["url"], box_size = 5, version = 5).convert("RGBA")
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 10 if "version" in app else 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
					if "version" in app:
						draw.text(((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2 + img.height), app["version"][:img.width//6], (0, 0, 0))
				qr.save(os.path.join("..", "assets", "images", "qr", webName(item) + ".png"))
				if not "qr" in app:
					app["qr"] = {}
				app["qr"][item] = "https://db.universal-team.net/assets/images/qr/" + webName(item) + ".png"

	if "prerelease" in app:
		for item in app["prerelease"]["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["prerelease"]["downloads"][item]["url"], box_size = 5, version = 5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0xF6, 0x6A, 0x0A, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 10 if "version" in app["prerelease"] else 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
					if "version" in app["prerelease"]:
						draw.text(((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2 + img.height), app["prerelease"]["version"][:img.width//6], (0xF6, 0x6A, 0x0A))
				qr.save(os.path.join("..", "assets", "images", "qr", "prerelease", webName(item) + ".png"))
				if not "qr" in app["prerelease"]:
					app["prerelease"]["qr"] = {}
				app["prerelease"]["qr"][item] = "https://db.universal-team.net/assets/images/qr/prerelease/" + webName(item) + ".png"

	if "nightly" in app:
		for item in app["nightly"]["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["nightly"]["downloads"][item]["url"], box_size = 5, version = 5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0, 0, 0xC0, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
				qr.save(os.path.join("..", "assets", "images", "qr", "nightly", webName(item) + ".png"))
				if not "qr" in app["nightly"]:
					app["nightly"]["qr"] = {}
				app["nightly"]["qr"][item] = "https://db.universal-team.net/assets/images/qr/nightly/" + webName(item) + ".png"

	# Add to output json
	output.append(app)

	# Website file
	web = app.copy()
	web["layout"] = "app"
	if "long_description" in web:
		web.pop("long_description")
	if not "systems" in web:
		web["systems"] = ["3DS"] # default to 3DS
	if not "updated" in web:
		web["updated"] = "---"
	for system in web["systems"]:
		if "title" in web:
			with open(os.path.join("..", "_" + webName(system), webName(web["title"]) + ".md"), "w", encoding="utf8") as file:
				file.write("---\n" + yaml.dump(web) + "---\n")
				if "long_description" in app:
					file.write(app["long_description"])

	if not "unistore_exclude" in app or app["unistore_exclude"] == False:
		# Add entry for UniStore
		uni = {
			"info": {
				"title": ucs2Name(app["title"]) if "title" in app else "",
				"version": ucs2Name(app["version"]) if "version" in app else "",
				"author": ucs2Name(app["author"]) if "author" in app else "",
				"category": app["categories"] if "categories" in app else [],
				"console": app["systems"].copy() if "systems" in app else [],
				"icon_index": len(icons) - 1 if "icon" in app or "image" in app else -1,
				"description": ucs2Name(app["description"]) if "description" in app else "",
				"screenshots": [],
				"license": app["license"] if "license" in app else ""
			}
		}

		if "updated" in app:
			uni["info"]["last_updated"] = parser.parse(app["updated"]).strftime("%Y-%m-%d at %H:%M (UTC)")

		if "screenshots" in app:
			for screenshot in app["screenshots"]:
				if screenshot["url"][-3:] == "png" and "horihd" not in screenshot["url"]:
					uni["info"]["screenshots"].append(screenshot)

		if "DS" in uni["info"]["console"]:
			uni["info"]["console"].remove("DS")
			uni["info"]["console"].append("NDS")

		# If scripts are specified, use those instead of the release files
		if "scripts" in app:
			for script in app["scripts"]:
				uni[script] = app["scripts"][script]
		
		# If autogen_scripts is forced or no scripts, generate scripts from downloads
		if "autogen_scripts" in app and app["autogen_scripts"] or not "scripts" in app:
			if "downloads" in app:
				for file in app["downloads"]:
					if len(re.findall("(zip|rar|7z|torrent|tar)", file)) == 0:
						uni[file + ((" (" + byteCount(app["downloads"][file]["size"]) + ")") if "size" in app["downloads"][file] else "")] = downloadScript(file, app["downloads"][file]["url"])

			if "prerelease" in app:
				for file in app["prerelease"]["downloads"]:
					if len(re.findall("(zip|rar|7z|torrent)", file)) == 0:
						uni["[prerelease] " + file + ((" (" + byteCount(app["prerelease"]["downloads"][file]["size"]) + ")") if "size" in app["prerelease"]["downloads"][file] else "")] = downloadScript(file, app["prerelease"]["downloads"][file]["url"])

			if "nightly" in app:
				for file in app["nightly"]["downloads"]:
					if len(re.findall("(zip|rar|7z|torrent)", file)) == 0:
						uni["[nightly] " + file + ((" (" + byteCount(app["nightly"]["downloads"][file]["size"]) + ")") if "size" in app["nightly"]["downloads"][file] else "")] = downloadScript(file, app["nightly"]["downloads"][file]["url"])

		unistore["storeContent"].append(uni)

# Make t3x
with open(os.path.join("temp", "icons.t3s"), "w", encoding="utf8") as file:
	file.write("--atlas -f rgba -z auto\n\n")
	for icon in icons:
		file.write(icon + "\n")
os.system("tex3ds -i " + os.path.join("temp", "icons.t3s") + " -o " + os.path.join("..", "unistore", "universal-db.t3x"))

# Increment revision if not the same
if unistore != unistoreOld:
	unistore["storeInfo"]["revision"] += 1

# Write unistore to file
with open(os.path.join("..", "unistore", "universal-db.unistore"), "w", encoding="utf8") as file:
	file.write(json.dumps(unistore, sort_keys=True))

# Write output file
with open(os.path.join("..", "data", "full.json"), "w", encoding="utf8") as file:
	file.write(json.dumps(output, sort_keys=True))

# RSS feed
# Get last update from old feed
oldUpdate = parser.parse("1970-01-01T00:00:00Z")
if os.path.exists(os.path.join("..", "index.rss")):
	r = untangle.parse(os.path.join("..", "index.rss"))
	oldUpdate = parser.parse(r.rss.channel.item[0].pubDate.cdata if type(r.rss.channel.item) == list else r.rss.channel.item.pubDate.cdata)

feedItems = []
latestUpdate = parser.parse("1970-01-01T00:00:00Z")
output.sort(key=lambda item: item["updated"] if "updated" in item else "---", reverse=True)
for item in output:
	if "updated" in item and parser.parse(item["updated"]) > latestUpdate:
		latestUpdate = parser.parse(item["updated"])

	if "updated" in item and (datetime.datetime.now(datetime.timezone.utc) - parser.parse(item["updated"])).days < 7:
		feedItems.append(rfeed.Item(
			title = item["title"] + " updated to " + item["version"] if "version" in item else "new version",
			link = "https://db.universal-team.net/" + webName(item["systems"][0]) + "/" + webName(item["title"]),
			description = (item["version_title"] if "version_title" in item else item["version"]) + (("<hr />" + item["update_notes"] if "update_notes" in item else "")),
			author = item["author"],
			guid = rfeed.Guid("https://db.universal-team.net/" + webName(item["systems"][0]) + "/" + webName(item["title"])),
			pubDate = parser.parse(item["updated"]),
			categories = item["systems"],
			extensions = [
				rfeed.Enclosure(
					url = item["image"],
					length = len(requests.get(item["image"]).content),
					type = "image/png"
				) if "image" in item else None
			]
		))

if len(feedItems) > 0 and latestUpdate > oldUpdate:
	feed = rfeed.Feed(
		title = "Universal-DB",
		link = "https://db.universal-team.net",
		description = "A database of DS and 3DS homebrew",
		language = "en-US",
		lastBuildDate = datetime.datetime.now(),
		pubDate = datetime.datetime.now(),
		items = feedItems,
		image = rfeed.Image(title = "Universal-DB", url = "https://universal-team.net/images/icons/universal-team.png", link = "https://db.universal-team.net"),
	)

	with open(os.path.join("..", "index.rss"), "w", encoding="utf8") as file:
		file.write(feed.rss())
