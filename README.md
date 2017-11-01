Templater.py

	A simple python program to build websites by generating html files from template files.
	By Ava Cordero

Overview

	Template or "fodder" files used are in .fdr format.

	Main template file is always ./template.fdr . It includes the main headers and menus you wish to include in every page of the website. Ithould be formatted as html code, and delineated with the marker "<!-- TEMPLATE PAUSES HERE -->" at the point in the document where the fodder content will be injected. There are optional markers for human readability, but this is the only marker that Templater.py will need in order to create a full webpage from a .fdr template file.

	"Fodder" files are stored in ./fodder/*.fdr . These content files will be combined with the template file to create webpage html files. ./fodder/*.fdr includes all content files to be injected into the website on a basic execution (no arguments). These can be optionally empty, or contain html code. You can include as many fodder files as you'd like.

	Output html files are stored in ./output/*.html or ./output.html and all are automatically logged to ./logs/output<datetime>/ or ./logs/output<datetime>.html , respectively, on subsequent executions.

	Please be aware .css and .js files need to be provided for your website separately, but all fodder files can be set to reference your resource files.

	There is example data stored in the ./fodder/ folder, which can be run with the basic execution (no arguments) to generate a website in the ./output/ folder. You can copy the ./assets/ folder to inside the ./output/ folder in order to examine the example website with full css and javascript functionality.
	
Usage

	./templater.py {fodder.fdr | default}

	The fodder.fdr argument will generate one webpage based on ./fodder/*.fdr and output the html file in ./output/*.html .
	The default argument will build one webpage based on the template and output the html file in ./output.html.
	Running the program without any arguments will create a website based off *all* .fdr files in ./fodder/ and output corresponding .html files in ./output/ .
