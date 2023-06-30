    var converter = new showdown.Converter();

    fetch('journal.md')
      .then(function(response) {
        return response.text();
      })
      .then(function(markdown) {
        var html = converter.makeHtml(markdown);
        var journalDiv = document.getElementById("journal");
        journalDiv.innerHTML = html;
      })
      .catch(function(error) {
        console.log('Error:', error);
      });
