window.onload = function(){

	// ========================================================
	let elementsToResize = []
	let $overlay = document.querySelector(".overlay")
	let $header = document.querySelector("header")
	let $content = document.querySelector("content")
	let $header_right = document.querySelector(".header__right")
	// ========================================================
	if ($overlay != null)
		$overlay.style.height = window.innerHeight - $header.clientHeight + "px"
	$content.style.minHeight = window.innerHeight - $header.clientHeight - getComputedStyle($content, "").padding.slice(0,2) * 2 + "px"
	if (window.innerWidth <= 1055)
		$header_right.style.justifyContent = "flex-start"
	else
		$header_right.style.justifyContent = "flex-end"
	
	
	window.addEventListener('resize', function(event){
		if ($overlay != null)
		$overlay.style.height = window.innerHeight - $header.clientHeight + "px"
  		$content.style.minHeight = window.innerHeight - $header.clientHeight - getComputedStyle($content, "").padding.slice(0,2) * 2 + "px"
  		if (window.innerWidth <= 1055)
		$header_right.style.justifyContent = "flex-start"
	else
		$header_right.style.justifyContent = "flex-end"
  		
	});
}