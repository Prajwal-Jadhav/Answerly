var simplemde = new SimpleMDE({ element: document.querySelector("textarea") });

simplemde.codemirror.on("change", function(){
	console.log(simplemde.value());
});