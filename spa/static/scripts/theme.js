(() => {
	const theme = localStorage.getItem('theme');

	if (theme) {
		if (theme === 'light') {
			document.documentElement.classList.remove('dark');
		} else {
			document.documentElement.classList.add('dark');
		}
	} else {
		localStorage.setItem('theme', 'dark');
		document.documentElement.classList.add('dark');
	}
})();
