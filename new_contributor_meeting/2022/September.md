###### tags: `new contributors meetings`
# Matplotlib New Contributors Meeting September 6th

Welcome to the monthly call for new contributors to the Matplotlib project 🎉

* Next meeting: September 6th, 2022 (Tuesday) @ 5PM UTC
* Join via [Zoom](https://us06web.zoom.us/j/81285851006?pwd=Tks2QjRkNWh5NGw0TmU1RUwwOVluZz09)
	* if you need a passcode for zoom MPL should work
* Our next meeting will be on:
	* October 4th, 2022 (Tuesday) @ 5PM UTC

### Code of Conduct

We want to take a moment to remind you that this meeting, like all project spaces is meant to be open, welcoming, diverse, inclusive, and it's important for us to have a healthy community. Like all matplotlib spaces, and everyone participating in them, this meeting will follow our [code of conduct](https://github.com/matplotlib/matplotlib/blob/main/CODE_OF_CONDUCT.md). If you haven't read it yet, please take some time to do so later on as it already applies to you. For now, in short, please be kind and generous towards one another. 

## Agenda

**Present:** Noa Tamir (@noatamir), Greg Lucas (@greglucas), Melissa Mendonça (@melissawm), Stefanie Molin (@stefmolin)
> please add your names (and github handle in brackets). This will makes it easier to stay in touch later in Gitter and on issues and pull requests (PRs) 😉
> This is optional since these notes will be recorded in our Github repository. If you'd like you can also paste your answer in the zoom chat 😉

*Feel free to add items for discussion to this agenda!*

* Introductions: 
	* Name 
	* A bit about our experience with matplotlib/python as users
	* Newcomer: why are we interested to start working with the project
	* Maintainer/contributor: how long have we worked with the project and what do we primarily do
* [name=Noa Tamir] Contributor Experience Lead, she/היא/sie
	* I joined Matplotlib in March so I'm relatively new as well. At the moment I am mostly working on documenation, and contributor exprience related issues (for example organizing this meeting).
* [name=Greg Lucas] Matplotlib Maintainer he/him
	* I joined Matplotlib about a year ago, but have been using it for quite some time now. I come from an Earth modeling and satellite data analysis background. In that regard, I am also a maintainer of another Python package, Cartopy, for plotting the data I work with on maps within Matplotlib.
> Newcomers please add items to the agenda based on your interests! What would you like us to discuss? do you want to ask something? are you already working on a specific PR? you can add a link to it ✨ Would you like to get some guidance on how to navigate some of the code? OR learn how to add a test? We will do our best to answer or help you connect you with the right people ☺️
* How do you pronounce CartoPy? Py like pie or like pea. 
    * Anyway you like! but Greg uses Pie.
* Discussion about GitPod and usefulness for getting contributors up and running more easily
    * Working through Numpy's setup https://github.com/numpy/numpy/blob/main/.gitpod.yml and a quick demo from @noatamir 
    * 50 hours free for individuals/month, then you can get a pro account if you're an open-source contributor
* You can use https://github.com/matplotlib/mpl-docker
* [Cakebrew for mac](https://www.cakebrew.com/)
* https://github.com/matplotlib/matplotlib/pull/23698/files Why aren't the SVG tests running? Is the SVG test actually required? The PNG test is available. 
    * Is SVG preferred because of text placement, or file size?
    * Is [Inkscape](https://inkscape.org/) installed? 
        * clarify this is required "for SVG comparison test"
        * https://github.com/matplotlib/matplotlib/blob/1d5221b2c5fe989fa6e7eb680839a1586cfa4d1e/lib/matplotlib/testing/compare.py#L232
        * https://github.com/matplotlib/matplotlib/blob/1d5221b2c5fe989fa6e7eb680839a1586cfa4d1e/lib/matplotlib/testing/compare.py#L139
        * Let's add this here: https://matplotlib.org/devdocs/devel/testing.html#writing-an-image-comparison-test
        * clarify both ghostscipt and inkscape requirements for image testing based on above links.
        * cross reference with https://matplotlib.org/devdocs/devel/dependencies.html#development-dependencies
    * @IGuKs80UTJCig4yt6Zos7w wonders why SVG would need an image comparison versus just the text output from the SVG file. (i.e. text diff vs image diff).
    * Perhaps have a few SVG image rendered specific tests, but if someone adds a new SVG file can text-based comparison work on the platform without needing to install inkscape?
    * Turn the "Dependencies for Matplotlib" into a table?
        * Add the place where the dependency is needed (docs, tests, code, ...)
        * Might be useful: https://sphinx-design.readthedocs.io/en/latest/
        

## Useful Resources

* [Our contributor Guide](https://matplotlib.org/devdocs/devel/contributing.html)
* This is where we keep past meeting notes from the new contributors meeting [on github](https://github.com/matplotlib/ProjectManagement)
    * You will soon find today's meeting notes there
	* You can also have a look at topics and links that were shared before 🧐
* If you are curious, here's an article about [the architecture of Matplotlib](http://www.aosabook.org/en/matplotlib.html)

### Communication channels

How will we communicate asynchronously while working on the project?
* [Gitter](https://gitter.im/matplotlib/matplotlib)
	* A chat platform which is useful for shorter questions
	* #incubator channel, our non-public communication channel for new contributors 
		* Ask Noa on chat now, or later on gitter to be invited
* [Discourse](https://discourse.matplotlib.org/)
	* A forum platform which is useful for longer questions that are harder to ask on chat 
* [Developer mailing list](https://mail.python.org/mailman/listinfo/matplotlib-devel)
	* We publish information which is important for contributors on this list. People from other projects might also share useful information or questions here. That said, it is also mirrored on our discourse 😉 (unless we there's a technical issue like happened recently 🙄)