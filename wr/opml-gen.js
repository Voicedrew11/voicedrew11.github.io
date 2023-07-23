/* Add an event that fires when the HTML document has been completely parsed,
   and all deferred scripts have downloaded and executed */
window.addEventListener("DOMContentLoaded", (event) => {
	/* List of webring website feeds in an Array */
	let feeds = [
		"https://voicedrew.xyz/rss.xml",
		"https://risingthumb.xyz/Writing/Blog/index.rss",
		"https://foreverliketh.is/blog/index.xml",
        "https://whitevhs.xyz/articles/atom.xml",
        "https://www.zeropointfool.com/feed/",
        "https://tilde.team/~zinricky/atom.xml",
        "https://sizeof.cat/socl.xml",
        "https://freckleskies.neocities.org/rss.xml",
		"https://microbyte.neocities.org/index.xml",
		"https://i330.dev/posts.rss",
		"https://starbreaker.org/feed.xml",
		"http://fetchrss.com/rss/64bb38d853d3b3072d6df25264bb38c9b086ac04a47d6512.xml",
		"https://aboboracandy.neocities.org/feed.xml",
	];
	/* Function that downloads the content of the text parameter to a text
	   file */
	function download(text) {
		const link = document.createElement("a");
		link.setAttribute("href", "data:text/plain;charset=utf-8," +
			encodeURIComponent(text));
		link.setAttribute("download", "Webring.opml");
		if (document.createEvent) {
			var ev = document.createEvent("MouseEvents");
			ev.initEvent("click", true, true);
			link.dispatchEvent(ev);
		} else {
			link.click();
		}
	}
	/* Event handler to call when the visitor clicks on the element with the
	   id `export-opml` */
	document.querySelector("#export-opml").addEventListener("click", (event) => {
		let last_update = new Date();
		let url_path;
		let opml = '<?xml version="1.0" encoding="UTF-8"?>\n' +
			'<opml version="2.0">\n' +
			'<head>\n' +
				'\t<title>Travelers of Agora Road</title>\n' +
				'\t<dateModified>' + last_update.toISOString() + '</dateModified>\n' +
			'</head>\n' +
			'<body>\n' +
				'<outline text="Travelers of Agora Road">\n';
		/* For each feed in the Array, build the XML structure */
		feeds.forEach((element, index) => {
			url_path = (new URL(element));
			opml += '\t<outline title="' + url_path.hostname + '" text="' +
				url_path.hostname + '" type="rss" xmlUrl="' + element + '"/>\n';
		});
		opml += '</outline>\n' +
			'</body>\n' +
			'</opml>\n';
		download(opml);
		event.preventDefault();
	}, false);
});
