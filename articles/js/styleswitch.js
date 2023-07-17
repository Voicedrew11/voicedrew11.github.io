function changeStylesheet(url) {
  // Create a new <link> element
  var linkElement = document.createElement('link');
  linkElement.rel = 'stylesheet';
  linkElement.href = url;

  // Find the existing <link> element
  var oldLinkElement = document.querySelector('link[rel="stylesheet"]');
  
  // Replace the old <link> element with the new one
  if (oldLinkElement) {
    oldLinkElement.parentNode.replaceChild(linkElement, oldLinkElement);
  } else {
    // If no existing <link> element is found, append the new one to the <head> element
    document.head.appendChild(linkElement);
  }
}
