# Matplotlib Weekly Meeting 

[![hackmd-github-sync-badge](https://hackmd.io/jd_7FjxNQ4y7XgNknvmvGQ/badge)](https://hackmd.io/jd_7FjxNQ4y7XgNknvmvGQ)

**A regular sync meeting for the project's maintainers, which is open to the community.** Everyone is welcome to attend and contribute to conversations.

## 27 July 2023 -- 


###### tags: `2023 dev call`


Call co-ordinates:  Thursdays @ 21:00 Berlin time (20:00 UTC during winter, 19:00 UTC during summer) https://zoom.us/j/384435716?pwd=WFpxVWxoYXArTDFzN1lWaHNoOE8xZz09

Previous notes: [Meeting Agendas](https://hackmd.io/zljR-pZrQ0O5J_j4NZ-9yw)
Archive: [matplotlib/ProjectManagement](https://github.com/matplotlib/ProjectManagement)

#### [Needs discussion at some point](https://hackmd.io/uzWviu8zSUChq3XhI2FqPg)

#### [Medium sized projects](https://hackmd.io/GgtrcXTlTfuoyHO76_LMLg)

#### [RSE worklog](https://hackmd.io/@matplotlib/HyVoUHlSo)

```
2023-04-20 19:00:00+00:00
Europe/Berlin        2023-04-06 21:00:00+02:00
UTC                  2023-04-06 19:00:00+00:00
America/New_York     2023-04-06 15:00:00-04:00
America/Vancouver    2023-04-06 12:00:00-07:00
US/Hawaii            2023-04-06 09:00:00-10:00
```
# 30 Nov 2023
## Agenda
 - [ ] discussion about moving time of standing meeting

# 23 Nov 2023

## Agenda
 - [ ] US thanksgiving

# 16 Nov 2023

_attending_: @tacaswell, @efiring, @ksunden, @QuLogic, @story645 

## Agenda
- [x] RSE updates
- [x] multi-line tags
- [ ] bug fix release 

## Notes

### RSE updates
 - Kyle: 
     - work on dataprototype
         - shape validation thinking + implemenation + tests
     - working on getting 3.8.2 out the door
         - one final PR with contours
 - Elliott
     - sick this week
     - waiting on follow up for igraph
     - webagg + jupyter RFB
     - found a bug in playwrite
     - will be putting in issues to upstream jupyter RFB
 - Tom
     - no mpl-gui work
     - working on making sure we are future proof

### multi line for tags
 - with many tags, can end up violating line length
 - multi-line tagging is a good idea, but not upstream yet

### 3.8.2 and 3.7.4

- xkcd script 
    - version from ipython repo is good enough
    - @story645 now has commit rights upstream
- contour label
    - PR coming
- wheel building for 3.7.4
    - may need to backport a couple more things
        - pin setuptools on azure
        - fix pinning on numpy on 32bit builds (or drop builds)

# 09 Nov 2023

## Agenda
_attending_ : @tacaswell @ksunden @chahak @efiring, @raphaelquast, @story645, @devRD, 


### New business
 - [x] RSE reports
 - [x] GSOD update

### Old business

### Issues and PRs
- [x] [name=raphaelquast] [overlapping axes](https://github.com/matplotlib/matplotlib/pull/27148)
- [ ] [name=raphaelquast] webagg improvements: [27160](https://github.com/matplotlib/matplotlib/pull/27160)
- [ ] [name=hannah] [humor sans to xkcd](https://github.com/matplotlib/matplotlib/pull/27299)
    - fork font? https://github.com/dummy-index/xkcd-font/raw/brushup/xkcd-script/font/ <-unmaintained fork
- [ ] [name=hannah] [path/xkcd](https://github.com/matplotlib/matplotlib/pull/26854#issuecomment-1804098144)
    - deperecate xkcd? interaction with [sketch seed](https://github.com/matplotlib/matplotlib/pull/26050)
 
## Notes

### RSE updates
 - Kyle
     - tracked down segfault with py312
     - data prototype work
 - Elliott
 - Tom
    - some mpl-gui work


### GSOD update
 - met deliverables
 - writing up case study + blog post to close out project
 - will keep an open doc meeting going
     - bi-weekly or monthly
 - remove from standing agenda starting next week

### webagg
- add feature as a go fast opt in, use string to denote alogorithm choice for flexibility

#### xkcd
- @tacaswell will talk to ipython about merging font
- make plt.xkcd discouraged rather than deprecated

# 02 Nov 2023

## Agenda
_attending_ : @greglucas, @story645, @rcomer , @efiring, @tacaswell, @ksunden, @qulogic, 


### New business

 - [x] RSE reports
 - [x] GSOD update
     - https://matplotlib.org/devdocs/devel/tag_guidelines.html
     - https://matplotlib.org/devdocs/devel/tag_glossary.html
 - [x] invited for full CZI EOSS6 propsoal

### Old business

 - [x] RFB update
 - [ ] [name=tacaswell] mpl-gui

### Issues and PRs
- [ ] [name=jklymak] [Logging versus warning vs...](https://github.com/matplotlib/matplotlib/issues/23422) and for [legend](https://github.com/matplotlib/matplotlib/issues/27145)
    - general: should we warn on valid input?
        - what should we name the warning if we do?
        - should warnings be toggleable?
    - general: should we use logging at all?
    - specific: should this particular instance (all numeric strings that get passed to categorical) get a message at all? 
- [ ] [name=oscargus] [Typing of values ending up in Text](https://github.com/matplotlib/matplotlib/pull/26867) 
    - Text converts to str independent of input data
    - Type as Any, document as str as @timhoffm suggests? (Makes sense to me.)
- [ ] [name=oscargus] [set/get_linestyle and dashed and ...](https://github.com/matplotlib/matplotlib/pull/23056)
    - If I have time to prepare a presentation and @timhoffm is present
- [ ] [name=oscargus] [Symlog hexbin](https://github.com/matplotlib/matplotlib/pull/22718)
    - Review needed, long waiting (make sure it is squash-merged)
- [ ] [name=rcomer] [Absolute values for pie](https://github.com/matplotlib/matplotlib/pull/25757) what should parameters be?

## Notes

### RSE updates
 - Kyle: 
     - 3.8.1 tagged and out
     - starting to work on NASA data stuff
 - Elliott
     - follow up from last work (docs, notebook/web backend)
     - still a few kinks in RBF (mostly snapshot on save)
     - all of toolbar but download button is working
 - Tom
     - met with Kyle on NASA data prototype
     - work on mpl_gui
     - pydataNYC sprints

### GSOD
 - sprints at pydataNYC
 - have built tag guidelines and glossary
 - got spreadsheet of tags via sprint, will convert to a PR
     - still working out best way to do that
 - Eva has notes about how to improve docs based on volunteers using them
 - meeting tomorrow for next steps



# 26 Oct 2023

## Agenda

_attending_: @tacaswell @trygve @devRD @ksunden @rcomer @IGuKs80UTJCig4yt6Zos7w (greg?) @chahak, @timhoffm, @story645 

### New Business

- [x] RSE reports
- [x] GSOD
- [x] [name=QuLogic] Jupyter-RFB proof of concept

### Issues and PRs

- [x] [name=hannah] [standard internal variable name for transforms](https://github.com/matplotlib/matplotlib/issues/22156)
    - do we want to standardize? if so which names? document this?

## Notes
- intros

### RSE reports

- kyle
    - PR review
    - 3.8.1 prep
    - went to xarray dev meetings for `NamedArray` pulled out (xarray variable pulled out with less dependencies)
- Elliott
    - docs things
    - 3.8.1 prep
    - proof-of-concept using jupyter RFB
    - pybind11 conversion

### jupyter RFB
- jupyter notebook 8 breaks nbagg
- never worked in jupyterlab, now broken in normal notebook
    - we did less than secure things to inject our js + comms
- RFB (remote frame buffer) will send you back user input, you send it bytes
- have a working prototype, only a few hundred lines
- questions
    - do we want to have this in main library?
    - do we want to push this to ipympl?
    - drop our notebook integration altogether and just rely on?
- how does js get served in jupyter?
    - do versions in the server env and kernel envs have to match?
    - js is installed in server side independent of the Python version in the kernel
    - but matching can be a range

### GSOD
 - going well
 - need to get PR merged by Tuesday for the sprint (so we can point at devdocs)
- tagging guidelines: https://github.com/matplotlib/matplotlib/pull/26851
- how tags look in gallery: https://github.com/matplotlib/matplotlib/pull/27083

### issues 
 - absolute pie values formatting
     - not a 5 minute conversation because the holding point is naming / parameters
 - standardize names
     - 

# 19 Oct 2023

## Agenda

_attending_: @rcomer, @ksunden, @chahak, @jklymak,  devRD, @melissawm esibinga, @story645, @efiring, @QuLogic 

### New Business

- [x] RSE reports
- [x] GSOD
- [x] Zenodo citation

### Issues and PRs
- [x] [name=ksunden] [hexbin mincnt](https://github.com/matplotlib/matplotlib/issues/27103)
- [ ] [name=jklymak] [Logging versus warning vs...](https://github.com/matplotlib/matplotlib/issues/23422) and for [legend](https://github.com/matplotlib/matplotlib/issues/27145)
    - general: should we warn on valid input?
        - what should we name the warning if we do?
        - should warnings be toggleable?
    - general: should we use logging at all?
    - specific: should this particular instance (all numeric strings that get passed to categorical) get a message at all? 
- [ ] [name=oscargus] [Typing of values ending up in Text](https://github.com/matplotlib/matplotlib/pull/26867) 
    - Text converts to str independent of input data
    - Type as Any, document as str as @timhoffm suggests? (Makes sense to me.)
- [ ] [name=oscargus] [set/get_linestyle and dashed and ...](https://github.com/matplotlib/matplotlib/pull/23056)
    - If I have time to prepare a presentation and @timhoffm is present
- [ ] [name=oscargus] [Symlog hexbin](https://github.com/matplotlib/matplotlib/pull/22718)
    - Review needed, long waiting (make sure it is squash-merged)
- [ ] [name=hannah] [standard internal variable name for transfroms](https://github.com/matplotlib/matplotlib/issues/22156)
    - do we want to standardize? if so which names? document this? 
- [x] [name=hannah] maybe sprint/good-first-issue project: [quoted rcParams](https://github.com/matplotlib/matplotlib/issues/3670)

## Notes

### RSE reports
- @ksunden: pytest with meson; lots of issues with that are not compatible with each other.  In particular how editable installs work.
    - not able to find pyc files
    - have work arounds that are being worked around
    - `pytest` versus `python -m pytest`
    - hexbin mincnt parameter
    - 3.8.1
- @QuLogic 
    - pybind11
    - website issues; proper redirects
    - real redirects instead of html files.  Canonical is set; maybe sitemap could be autogenerated 


### GSOD
- tagging sprint beginning Nov.
- categories and subcategories
- google spreadsheet tagging workflow
- 1/3 tagged for examples before sprint

### Zenodo citations
- now generic, doesn't pull from github anymore
- github stats run anyways on milestone
- maybe pull and populate cff file

### hexbin 
- `mincnt` comparison `>` to `>=`, `mincnt=0`, some reduction functions error
    - default reduction is `mean` but returns nan. `max` returns error.
- solutions:
    - go back to `>`
    - make default 1
    - make default change with functions depending on their behaviour
- decision: make default 1, update docstring to clarify that users can set to 0

### quoted rcParams

See https://github.com/matplotlib/matplotlib/issues/3670#issuecomment-1771672120


-----

# 12 Oct 2023

_attending_: @rcomer, @tacaswell, @efiring, @ksunden, @jklymak, @devRD, @QuLogic, @trygve, @story645 

### Agenda


### Old Business

### New Business

- [x] RSE reports
- [x] GSOD

### Issues and PRs
- [x] [name=jklymak] [contour: allsegs, alltypes](https://github.com/matplotlib/matplotlib/issues/26913) remove depreaction?
- [x] [name=jklymak,anntzer] [access to colorbar's formatters/locators](https://github.com/matplotlib/matplotlib/issues/26896)
- [ ] [name=oscargus] [Typing of values ending up in Text](https://github.com/matplotlib/matplotlib/pull/26867) 
    - Text converts to str independent of input data
    - Type as Any, document as str as @timhoffm suggests? (Makes sense to me.)
- [ ] [name=oscargus] [set/get_linestyle and dashed and ...](https://github.com/matplotlib/matplotlib/pull/23056)
    - If I have time to prepare a presentation and @timhoffm is present
- [ ] [name=oscargus] [Symlog hexbin](https://github.com/matplotlib/matplotlib/pull/22718)
    - Review needed, long waiting (make sure it is squash-merged)
- [x] [name=hannah] [mypy pre-commit hook](https://github.com/matplotlib/matplotlib/pull/26954)
    - was there consensus last week?  
- [x] [name=hannah] [list of dicts path.effects param](https://github.com/matplotlib/matplotlib/pull/26854)
    - feedback on whether this is feasable 
- [x] pytest + meson conflict?


## Notes

### RSE reports
- @ksunden data prototyping; 
    - scatter prototype.
    - 3.8.1 release close; couple of RC
- @QuLogic 
    - pybind 11
    - EOSS grant
- @tacaswell 
    - EOSS grant
    - MPL GUI now has pyplot-like module; docs forthcoming
    
### GSOD
- going well
- Eva is doing more tagging
- working on a sample page with melissa

### Issues and PRs

- mypy precommit
- Remove deprecate allsegs, find_nearest_contour... @jklymak will PR
- "long_axis" exposed as a read-only property.  @jklymak will PR
- patheffects: dictionary cannot have "name" as it can possibly conflict with a keyword to patheffects classes that may be called "name".
- meson and pytest: not consulting result source code
    - pytest not consulting metapath?
    - try passing `--import-mode importlib`


------

# 5 Oct 2023

## Agenda
_attending_: @tacaswell, @jklymak, @ksunden, @haoyingzhang, @efiring, @melissawm, @devRD, @trygve, @story645, @timhoffm, @QuLogic  

### Old Business

### New Business
- [x] RSE reports
- [x] GSOD: 
    - https://github.com/matplotlib/matplotlib/pull/26851
    - https://pydata.org/nyc2023/about/ Oct 31st
- [x] [name=hannah] hacktober policy

### Issues and PR:

- [x] [name=jklymak] [contour: allsegs, alltypes](https://github.com/matplotlib/matplotlib/issues/26913) remove depreaction?
- [x] [name=jklymak,anntzer] [access to colorbar's formatters/locators](https://github.com/matplotlib/matplotlib/issues/26896)
- [x] [name=jklymak] mpl-gui? https://github.com/matplotlib/mpl-gui
- [ ] [name=oscargus] [Typing of values ending up in Text](https://github.com/matplotlib/matplotlib/pull/26867) 
    - Text converts to str independent of input data
    - Type as Any, document as str as @timhoffm suggests? (Makes sense to me.)
- [ ] [name=oscargus] [set/get_linestyle and dashed and ...](https://github.com/matplotlib/matplotlib/pull/23056)
    - If I have time to prepare a presentation and @timhoffm is present
- [ ] [name=oscargus] [Symlog hexbin](https://github.com/matplotlib/matplotlib/pull/22718)
    - Review needed, long waiting (make sure it is squash-merged)
- [x] [name=hannah] [mypy pre-commit hook](https://github.com/matplotlib/matplotlib/pull/26954)
- [x] [name=hannah] [axisartist tables](https://github.com/matplotlib/matplotlib/pull/26754)
    - grid tables vs list tables 
- [ ] [name=hannah] [list of dicts path.effects param](https://github.com/matplotlib/matplotlib/pull/26854)
    - is this a viable direction to go in?
- [x] [name=ratna] Review needed.. [Stix table update](https://github.com/matplotlib/matplotlib/pull/26830/)
- [x] [name=haoying]  [QuiverKey error](https://github.com/matplotlib/matplotlib/issues/26316/)
    - Clarification of ``angle`` in [doc](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html)

## Notes

### RSE reports:
- @tacaswell: 
    - CZI letter of intent getting in, indicating new things to do, and carrying on current work
    - test image work plans
- @ksunden:
    - PR review; clabel for low dpi issue
    - hacktoberfest PRs
- @QuLogic 
    - meson merged for building. 
    - pybind11 - agg 
- @melissawm 
    - coming back from holidays.  Now on volunteer basis versus

### GSOD
- refactoring based on feedback
- tagging sprint Oct 31.  +general Matplotlib sprint  pydata NY. 
- https://github.com/matplotlib/matplotlib/pull/26851 review

### bivariate colormapping. https://github.com/matplotlib/matplotlib/pull/26996
- 2d colormaps versus multivariate
- VectorMappable instead of Scalar mappable
- pcolormesh implimentation.
- list of further changes.
- Is this way good?
    - how to roadmap it? 
- needs specific colormaps?

### Quiver Key 

- angle degrees anti clockwise from x axis versus horizontal

### hacktoberfest

- flag one liners or treat as normal
- _usually_ one liners are welcomed.
- Treat as normal.  Don't label, just close
- formatting changes OK

### MPL GUI
- attach GUI after figure made rather than figure needs a GUI to be instantiated.
- get into library or install into pypi first...
- see if people like it.
- Could be part of main...
    - iteration cycles...
- applications:
    - interactive use cases where helpful
    - API: distinguish from different interfaces.
- could have an experimental import of 3rd party library...
    - circular dependency
    - optional dependency?
- next week @tacaswell @timhoffm will try and look at it...
- would require  documentation changes, but after stable


### mypy pre-committ hook?
- runs on `lib/matplotlib/`
- some caching
- linter?

### grid versus list tables
- read more than edited
- spacing
- vim extension, VSCode
- longer tables OK as list table...
- 





----------
# 28 Sept 2023

## Agenda
_attending_: @tacaswell, @rcomer, @devRD, @oscargus, @haoyingzhang, @efiring, @theOehrly, @ananyadevarakonda, @ksunden, @jklymak, @story645, @qulogic, @rakshitsingh

### Old Business
- [x] GHC

### New Business
- [x] RSE reports
- [x] GSOD: https://github.com/matplotlib/matplotlib/pull/26851
- [x] [name=hannah] hacktober

### Issues and PR:

- [x] [name=jklymak] [timedelta64 support](https://github.com/matplotlib/matplotlib/pull/19236)
- [ ] [name=jklymak] [contour: allsegs, alltypes](https://github.com/matplotlib/matplotlib/issues/26913) remove depreaction?
- [ ] [name=jklymak,anntzer] [access to colorbar's formatters/locators](https://github.com/matplotlib/matplotlib/issues/26896)
- [ ] [name=jklymak] mpl-gui? https://github.com/matplotlib/mpl-gui
- [x] [name=oscargus] Rename "topic: types" to "topic: typing"?
    - Objections?
- [ ] [name=oscargus] [Typing of values ending up in Text](https://github.com/matplotlib/matplotlib/pull/26867) 
    - Text converts to str independent of input data
    - Type as Any, document as str as @timhoffm suggests? (Makes sense to me.)
- [ ] [name=oscargus] [set/get_linestyle and dashed and ...](https://github.com/matplotlib/matplotlib/pull/23056)
    - If I have time to prepare a presentation and @timhoffm is present
- [ ] [Symlog hexbin](https://github.com/matplotlib/matplotlib/pull/22718)
    - Review needed, long waiting (make sure it is squash-merged)

## Notes

### introductions

### GHC
 - got a good number of PRs (and ) datetime tests and deprecations

### RSEs
- @ksunden : all day at Grace Hopper, dealing with GHC issues (merge conflicts, CI), 
    - Typing `mypy --strict` reports pouring in.
    - eg `plt.show` is untyped and mypy fails.
    - meson discussions
- @QuLogic 
    - GHC things: about 15 PRs
    - cycler release candidate; testing trusterd publisher workflow
        - remove some cycler type hinting 
    - documentation site: redirects to clean up some of the setup so that many files can be moved out of top level
    - ISO 1202 cycling linestyles issue. Some interesting thoughts about implimentation of dashing.
        - standard is $200 or so to buy
        - long descriptive names?
        - straightforward to impliment
    - worth thinking about reviving LineStyle class work

### GSOD:
- tagging sprint?
    - good plan
- PR
    - please look at
    - discussion about separating the different domains the tags are pulled from (generic vs mpl specific)
    - how should this look in the docs?
    - how do we make sure it is clear that the number of docs can grow?
- how will this look when rendered in the docs?
    - will help evaluate how the tags are understood
    -``` .. tags:: tag1, tag2```
    - sample: https://napari.org/stable/gallery.html
### Hacktober
- no t-shirts; plant a tree
- datetime testing as easiest thing to steer people to
- put tags on, and help first PRs.  
- spam label if nuisance PRs
- "hacktober accepted" label for unmerged but worthy PRs

### Timedelta64
- either error better
- or use Timedelta64 as in PR.
- mark as provisional consider unstable for a cycle...
- need example for how to turn it off and changing defaults.
    - need to look at knobs for adjusting Locator and Formatter.
    - Whats new needs examples
- pandas Timedelta formatter as touchstone?
- stop at a day for largest interval
- Current version:
    - has knobs
    - @theOherly willing to work on this
    - string formatting? Define string formatter...
    - define a function formatter

### Comaptibility with pandas and CFtime:
- useful to rethink ways to lock out Locators and Formatters that are incompatible with a given unit converter so users are not confused when locators and formatters don't work.
- https://github.com/matplotlib/matplotlib/issues/24951

-------

# 21 September 2023

## Agenda
_attending_: @efiring, @ksunden, @tacaswell, @rcomer, @trygve, @haoyingzhanh, @jklymak, @devrd, @QuLogic, @story645 

### Old business

### New Business
- [x] RSE updates
- [x] GSOD updates
    - https://github.com/matplotlib/matplotlib/pull/26851
- [x] 3.8 release
    - typing fallout? 
    - [pandas](https://github.com/matplotlib/matplotlib/issues/26858)
- [x] GHC OSD prep
    - [ ] https://github.com/matplotlib/matplotlib/pull/26859
- [x] [name=hannah] [merge with single review label](https://github.com/matplotlib/matplotlib/labels/status%3A%20merge%20with%20single%20review%3F)
- [x] numfocus summit comments

### Issues and PRs
- [ ]  meta-limits https://github.com/matplotlib/matplotlib/issues/26442


## Notes

### RSE updates:
- @tacaswell: on family leave
- @ksunden: dealing with 3.8 release issues.  
    - np.ndarray not a `Sequence` but is acceptable input for many things.  "array-like" isn't correct because it accepts scalars. `np.ndarray` is missing index and count  
    - `plt.Axes` and `plt.Figure` not exported
    - locale issue
    - some optimizations had unexpected changes
- @QuLogic 
    - 3.8 fallout
    - CI automation
        - trusted-publishing on cycler
    - meson
        - https://github.com/matplotlib/matplotlib/pull/26621
        - makes c-extension work way easier
    - cirrus CI
        - https://github.com/matplotlib/matplotlib/pull/24597
        - currently passing, but numpy has been hitting caps
    - GHC OSD prep
        - have a lot of "good first issue" PRs
        - add issue for removing deprecations

### GSOD

- first draft of tags + tag guidelines
- Eva has been tagging things in a spreadsheet
- goal is to do tagging sprint at pydata NYC (November)
- looking for high-level feedback on categories
- private category?
    - tags on examples but not displayed on built page
- check if this is a good starting point
- levels
    - based on what context the reader to understand
- are there any controversial looking tags
    - things that would be hard for a new-contributor to follow rules and correctly apply tags

### NFSummit

- @rcomer attended last week in Amstredam
- discussions about writing a cook-book for universities for how to contribute to open source projects in a way that is easier on maintainers
- lots of biology projects

### single review merge label

can use if you want

### issues with sphinx version

### namespace packages

- why do we have a namespace package
    - historical reasons
- currently having (worse) issues with shadowing
- if you shadow something with a Matplotlib install which provides the mpl_toolkits importer will prefer the old one


options
 - move mpl_toolkits in wholesale
 - move just mplot3D

cons: by pulling it in we are sigining up to keep it alive forever


--------
# 14 September 2023

_attending_: @trygvrad, @jklymak, @ksunden, @IGuKs80UTJCig4yt6Zos7w (@greglucas), @QuLogic, @devRD , @haoyingzhang, @efiring, @story645  

### Old business
- [x] Steering team?

### New business
- [ ] RSE updates
- [ ] GSOD updates

### Issues and Pull requests

- [ ] [name=hannah] [move coc into users/project](https://github.com/matplotlib/matplotlib/pull/26702)
    - motivation is new landing page [about us](https://matplotlib.org/devdocs/#about-us)
- [ ] [Multivariate colormapping](https://github.com/matplotlib/matplotlib/issues/14168#issuecomment-1719170227)

## Notes

- steering council team: @QuLogic will work on it.

### RSE updates:
- @ksunden  
    - 3.8 Segfault reported so working on that (polar triangles with NaN values in Agg); 
    - release notes
- @QuLogic also 3.8 release; 
    - CI - new limits on Cirrus builds will have to watch; 
    - Working on Meson build - waiting on pybind11 for image module.  Also after 3.8;
        - no-build-isolation flags when building editable versus isolated VM
        - some notes in docs for developers
        - otehrwise should be similar
        - some concern for downstream that care about nightly wheels because version number labeller not trivial;
            - needs upstream work
        - advantage; auto recompile c extensions if edited versus having to remember to pip install..
    - mpl-sphinx-theme: automatic pushing to pypi.  Maybe try for 3.9 or 3.8.1 main library versus manually upload wheels.

### GSOD/GSOC
- @ratna 
    - post to front page news item. Need to fix sphinx pinning.
- GSOD:
    - no updates.

### Code of Conduct 
- move into `users/project` from `CODE_OF_CONDUCT.md`
- link goes to stable

### Mutlivariate colormapping

- types:
    - overlapping images with single colormaps 
        - meshing two images:
            - RGB matrices "added"
            - need to choose RGB so that adding is well-defined
    - 2-D colormap
        - designed 2-D colormaps
        - hsv colormaps, but uneven in colorspace
    - https://colorstamps.readthedocs.io/en/latest/
- implimentation options:
    - implicit 
        - set V colormaps or norms to trigger
        - (V, M, N)
        - Additive: colormap families needed to make sense
        - Two-d: separate bivariate norm and bivariate colormaps
        - ScalarMappable multiple norms?
            - Make a parent "Mappable" that allows multiple inputs to make a color.
            - use the Transform stack as a model maybe? _BaseMappable + dim dispatch
        - new methods as alts to `{plt, fig}.colorbar(ScalarMappable)`
            -  `multiple_colorbar(VectorMappable)` that positions multiple colorbars
            - `bivariate_color{square,circle}(VectorMappable)` + new class(es) for color square/circle object
    - explicit
        - separate methods.
    - third alternative: separate packages.



--------
# 07 September 2023

_attending_: @rcomer @devRD @jklymak @story645 @efiring @haoyingZhang @QuLogic 

### Old business
- [x] [name=hannah] [ipympl small dev grant](https://hackmd.io/NngZP7hTRVuPPHcnNFx8OA)

### New business
- [x] RSE updates
- [x] GSOC/GSOD updates
- [x] [name=hannah] [CZI EOSS round 6](https://chanzuckerberg.com/rfa/essential-open-source-software-for-science/)
- [x] add steering council [github team](https://github.com/orgs/matplotlib/teams)
    - would allow for finer grained permissions on governance

### pull requests 
- [ ] MPL GUI: https://github.com/matplotlib/mpl-gui Perhaps move to integration soon?



## Notes

### ipympl small dev grant?
- $10k...
- ipympl more usable, and similar as possible to other backends.
- limitation now: can't act on previous plot?
- compare w/ other similar backends 
- won't submit on this cycle, instead gather more info for submitting different round or as a larger grant 
- https://github.com/pyodide/matplotlib-pyodide
- https://github.com/matplotlib/ipympl

### RSE

### GSOC/GSOD

- @Ratna: GSOC ended.  Time off.  Draft PRs.  Final reports submitted.  Blog post.  Will send link to @story645 
- @story645: tagging sprint pydata Nov. Second draft on site by Oct.  First draft up soon?

### EOSS round 6
- will want to go for that, as much as we can get.
- [CZI EOSS round 6](https://chanzuckerberg.com/rfa/essential-open-source-software-for-science/)
- https://chanzuckerberg.com/wp-content/uploads/2023/08/EOSS-6-RFA-Packet-Final.pdf
- Maintenance of the project
- Steering council will discuss plans going forward.




----
# 31 August 2023

_attending_: @efiring, @IGuKs80UTJCig4yt6Zos7w @haoyingZhang, @story645 @QuLogic @devRD @timhoffm 

## Agenda

### Old business

### New business
- [x] RSE updates
- [x] GSOC/GSOD updates
- [x] 3.8rc
- [x] [name=hannah] pydata NYC, Nov 1-3
- [x] [name=hannah] small dev grant, Sept 8
- [x] [name=hannah] streamline approval of triage additions
- [ ] @qlogic PyCharm issue

### Pull requests
- [ ][name=hannah] [barh dict key](https://github.com/matplotlib/matplotlib/pull/26577)

## Notes


### RSE
- Kyle: largely 3.8rc; some with Seaborn, numpy 2.0 preparation. Did do some playing with data-prototype units behavior
- Elliott: typing large and small; mainly Meson #26621 should be close; docs coming soon.


### GSOC/GSOD
- Ratna: comments on open PRs; work on super/subscripts, spaced--looking for LaTeX behavior matching.
- Hannah (for Eva): fleshing out scoping; opened issues on Sphinx Gallery.

### 3.8rc
- Some typing cleanups to be done.
- Dictionary input to barh is broken by a typing change PR? Kyle will investigate.

### Pydata NY
Hannah will attend and probably do a sprint and maybe a joint tutorial; is anyone else coming?  Sept. 22 deadline for proposal (but it's flexible); only cost is travel.

### Small Devel Grant
Hannah talked with Ian Hunt-Isaak about mpl-playback, for gifs in gallery to show widget behavior; probably not enough work still needed.
- https://github.com/matplotlib/matplotlib/pull/23441
- https://github.com/matplotlib/matplotlib/pull/22634
- https://github.com/pyodide/matplotlib-pyodide

Concern about low-bandwidth functionality: there may be options for handling it.

Do we need a full html backend? Render to html; can see by opening in browser.

- Do we want another Quantstack SDG for ipympl improvement or replacement?
- Nicolas Rougier advocates a library-independent rendering protocol.  All libraries could take advantage of the various hardware optimizations.  Maybe an SDG could do a study preparatory to a massive project.
- Elliott: vispy was supposed to be an all-encompassing replacement of all 3D graphic libraries. While it didn't fully do that, there was a `jupyter_rfb` that came out of it that might be useful for `ipympl` as its implementation/replacement. https://jupyter-rfb.readthedocs.io/en/stable/
- Proposal from Hannah: SDG for ipympl maintenance? She will start a hackmd for listing things to fix.
    - https://hackmd.io/NngZP7hTRVuPPHcnNFx8OA

### backends for notebooks
Tim: better notebook backend is higher priority.

### streamline approval of triage additions
Proposal: send steering council "is this person OK to add" email? steering council has N days to say NO, maintainers have privileges to/can then add person

### PYCharm
#26463 (Tim has PyCharm and can check)  Elliot can't reproduce; maybe it is PyCharm version-specific, maybe fixed.

# 24 August 2023

_attending_: @efiring, @rcomer, @haoyingZhang, @ksunden, Eva Sibinga, @story645, @devRD, @QuLogic 

## Agenda

### Old business

### New business

- [x] RSE updates
- [x] GSOC/GSOD updates
- [x] 3.8rc
- [x] what systems are supported?

## Notes
### small dev grant
- mpl-playback has 50% feedback, question is how fast is good enough for doc builds
### tiny-icons
- numfocus lawyers are talking to tiny-icons

### RSE
 - ksunden: NASA annual report, responding to 3.8 issue reports (Seaborn today); with Elliot, looked through Fedora build failures; mostly minor
 - Elliot: Fedora: only 5 are new failures; bugs reported.  Nothing that we accidentally broke.  Work on Meson port, facilitated by work done for numpy and scipy.  Working on linux and Freetype versions.  Should be ready for 3.9.

### GSOC/GSOD
 - Eva: draft PR coming in next few days with guidelines for tagging gallery examples.  Includes examples of tags.
 - Ratna: GSOC final report deadline this week.  Some longterm issues depend on future work.  New features have been added.

### 3.8
Not too many complaints about backwards incompatibility.

### What systems do we support?

Whatever is reasonable: we can test it, and there is a developer.

Specific question: GTK on Mac?  Maybe; updating for newer GTK API is good, provided the code still works on older versions.

Testing of doc build on Windows? Maybe weekly? Hannah will investigate; requires command-line latex, etc.

# 17 August 2023

_attending_: @efiring, @ksunden, @haoyingZhang, @melissawm,
@chahakmehta, @oscargus, @devRD, @story645, @QuLogic, @rcomer

## Agenda

### Old business

### New business

- [X] RSE updates
- [X] GSOC/GSOD updates
- [X] 3.8rc
- [X] 3.9
- [x] small dev grant https://numfocus.org/programs/small-development-grants

## Notes

### Old
Plausible: instance set up, managed by scientific python project; Elliot will  contact Melissa via email regarding an address and contact.


### RSE
 - Kyle: new desktop set up. Annual report for NASA grant is underway.  responding to 3.8 bug reports; general maint. Fix sphinx
 - Elliott: mostly typing on mathtext; CI maint.; Cirrus is working, but should we enable it?  Other maint.
 - Melissa: "plausible", working on reports, winding down.

### GSOC/GSOD
 - Ratna: various mathtext features
 - Hannah: no update this week

### 3.8
 - Oscar: https://github.com/matplotlib/matplotlib/pull/26522 Do we need better validation?

### 3.9
 - Haoying: https://github.com/matplotlib/matplotlib/issues/26092
    - RGBA array + alpha kwarg input
        - scaler alpha: 
            - 2D and RGB - overwrites
            - RGBA - works, unclear if blend or overwrite
        - array alpha:
            - 2D array w/ colormap (no A): overwrites cmap(2d Array)(A=1)
            - 2D array w/ colormap w/ A: unknown cmap(2d Array)
            - RGB: ignores alpha -> RGB(A=1)
            - RGBA array: ignores
    proposed solutions:
    - ignore one alpha - either A or alpha
    - blend A and alpha - 
    - consensus: to consistenly blend, treat alpha=None as alpha=1
    
### small dev grant
Due... Sept 8
- mpl-playback: https://github.com/matplotlib/matplotlib/pull/23441


# 10 August 2023

_attending_: @efiring, @rcomer, @ksunden, @melissawm, @oscargus, @haoyingZhang, @devRD, @QuLogic, @story645, @chahakmehta, @anntzer, @tacaswell

## Agenda

### Old business

### New business

- [x] RSE updates
- [x] GSOC/GSOD updates
- [x] NF summit
- [x] 3.8rc1 is out!
- [x] 3.9 goals?

## Notes

### RSE
 - Thomas
     - clearing issues, helping with 3.8
 - Kyle
     - geting 3.8rc1 out the door
     - pypy wheel building / musl
 - Elliott
     - finishing up 3.8, ps work, doc work
 - Mellissa
     - working on grant report / wrapup
     - planning to do some doc work

### GSOC/GSOD

- Ratna (GSOC)
    - had a couple of stalled issues, currently working on resolving
    - was waiting on feedback on alignment which was gotten, dealing with consequences
- Hannah (GSOD)
    - there is a PR that needs review

### NF summit
- Ruth and Tim will be representing Matplotlib
- pass them anything we want to communicate to NF or other projects

### 3.8.0rc1

- please test!
- question about typing private methods
    - not done in first pass because it is aimed at down-stream tools
    - not done to try and put upper bound on initial work
    - we will take PRs to add types to private methods going forward

### 3.9 goals

- finish rcparams work (chahak)
- linestyles (from Oscar, need input from Tim)
- continue to (re)organize the docs
- backend selection improvements / pull in mpl-gui ()https://github.com/matplotlib/mpl-gui
- pull mplcairo into core?

### plausible (website analytic)
- scientific python has an instance

### symlog locater

- internal list is not ordered, should we fix it or just test the current behavior
    - decide to just leave

### 


# 03 August 2023
_attending: @efiring, @rcomer, @greglucas, @ksunden, @devRD, @tacaswell , @story645 

## Agenda

### Old business

### New business

 - [x] RSE updates
 - [x] GSOD / GSOC updates
 - [x] 3.8 rc?!
 - [ ] where to put the GSOD output: [organize docs devdocs](https://github.com/matplotlib/matplotlib/issues/26392)

## Notes
### updates
 - RSE update
     - Tom: where did july go?!  Some 3.8 work + behind the scenes work 
     - Kyle:
         - 3.8 prep
         - got the pyparsing fix commited upstream and backported to 3.7.x
         - working with xarray to deal with our coming type hints, at least one fix on our side
         - all main release critical stuff is done
     - Elliott: 
         - typing work for 3.8 (using mypy --strict and fixing small things)
         - mplsphinx-theme to upload automatically
 - GSOC
     - ok-ish
     - been working on a couple of issues that are not clear, waiting on feedback
     - looking at bold caligraphy
     - sized delimiters
 - GSOD
     - Eva has a couple of small PRs in the queue
     - text is getting ready
     - where to put it?
     - going well
     - 
### 3.8 progress

- one PR from @QuLogic with lots of little type hint fixes https://github.com/matplotlib/matplotlib/issues/26407
- tonight or tomorrow

### news

- we have a pypi org now

### orginize the docs

 - @story645 is going to start writing a documentation road map




# 27 July 2023

## Agenda

_attending_: @efiring, @jklymak, @ksunden, @devRd, @RaphaelQuast, @haoyingZhang, @qulogic, @story645

### Old business

### New business

 - [x] RSE updates
 - [x] [name=hannah] [Simple Icons permission](https://github.com/simple-icons/simple-icons/issues/3410#issuecomment-671602746)
 - [x] [name=hannah] [new docs labels](https://github.com/matplotlib/matplotlib/labels?q=document)
 - [ ] 3.8 outstanding issues

### PRs and Issues

- [x] [name=ratna] Hrule rendering: https://github.com/matplotlib/matplotlib/issues/23763
- [ ] [name=raphael] pan/zoom of overlapping axes https://github.com/matplotlib/matplotlib/pull/22347
- [ ] antialiasing in mathtext https://github.com/matplotlib/matplotlib/pull/26376


## Notes

### RSE updates
- @ksunden: reviews for 3.8 in particular (typing w/ Elliott)
- @QuLogic typing work, largely internal
- @Ratna: GSoC
    - mathtext.  Draft PRs (hrule, latin)
- @hannah: GSoD
    - second eval submitted, halfway through first pass tagging, private draft of tagging + content guidelines

### Typing
- new 3.8
- maybe some release strategy
- document for users, developers
- downstream projects: some comms at scipy as may affect them.
- Microsoft has some type hints that people have used.
    - project ones take precedence (probably)

### Hrule
-  Hrule rendering: https://github.com/matplotlib/matplotlib/issues/23763
    -  maybe clarify issue more
    - contact @anntzer with write up of problem and potential repair paths

### tiny icon
- https://github.com/simple-icons/simple-icons/issues/3410#issuecomment-671602746
    - trademark issue?
    - numfocus?
    - https://github.com/simple-icons/simple-icons/blob/develop/DISCLAIMER.md
- [x] @story645 emailed Numfocus & CCed steering-council

### Doc github labels
- more fine grained than before

### RC 3.8
- pyparsing issue; pinned for now
    - testing issue...
    - user facing in error handling...
- contouring antialiasing
    - re-adding property
    - some deprecations recommend deprecated properties

### pan/zoom of overlapping axes 
- https://github.com/matplotlib/matplotlib/pull/22347

### mathtext anti aliasing?
- needs review
- 3.8?
- https://github.com/matplotlib/matplotlib/pull/26376




