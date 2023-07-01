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
