const e1 = document.querySelector("textarea");
const stackedit = new Stackedit();

// Open the iframe
stackedit.openFile({
  name: 'Filename', // with an optional filename
  content: {
    text: el.value // and the Markdown content.
  }
});

// Listen to StackEdit events and apply the changes to the textarea.
stackedit.on('fileChange', (file) => {
  el.value = file.content.text;
});