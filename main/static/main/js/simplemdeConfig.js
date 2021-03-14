let simplemde = new SimpleMDE({ element: document.querySelector("#id_content") });
let textarea = document.querySelector("#id_content");


simplemde.codemirror.on("change", function () {
	textarea.value = simplemde.value();
});