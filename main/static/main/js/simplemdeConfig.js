let simplemde = new SimpleMDE({ element: document.querySelector(".simplemde_form textarea") });
let textarea = document.querySelector(".simplemde_form textarea");


simplemde.codemirror.on("change", function () {
	textarea.value = simplemde.value();
});