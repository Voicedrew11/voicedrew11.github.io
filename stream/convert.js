/*
function convertScript() {
  return new Promise(function(resolve, reject) {
       var converter = new showdown.Converter();

fetch('https://raw.githubusercontent.com/Voicedrew11/voicedrew11.github.io/Microsoft95/stream/journal.md')
  .then(response => response.text())
  .then(content => {
    // Process the content as needed
    var html = converter.makeHtml(content);
    var journalDiv = document.getElementById("journal");
    journalDiv.innerHTML = html;
  })
  .catch(error => {
    console.error(error);
  });

    resolve();
  });
}

function tocScript() {
tocbot.init({
      tocSelector: '.js-toc',
      contentSelector: '.js-toc-content',
      headingSelector: 'h1, h2, h3',
      hasInnerContainers: true,
        });
tocbot.refresh();
}

// Usage:
convertScript().then(function() {
  tocScript();
});
*/

var converter = new showdown.Converter();

function convertScript(callback) {
  fetch('https://raw.githubusercontent.com/Voicedrew11/voicedrew11.github.io/Microsoft95/stream/journal.md')
    .then(response => response.text())
    .then(content => {
      // Process the content as needed
      var html = converter.makeHtml(content);
      var journalDiv = document.getElementById("journal");
      journalDiv.innerHTML = html;

      // Call the callback function when finished
      callback();
    })
    .catch(error => {
      console.error(error);
    });
}

function tocScript() {
  tocbot.init({
    tocSelector: '.js-toc',
    contentSelector: '.js-toc-content',
    headingSelector: 'h1, h2, h3',
    hasInnerContainers: true,
  });
  tocbot.refresh();
}

// Usage:
convertScript(function() {
  // This anonymous function will be called when convertScript has finished executing
  tocScript();
});
