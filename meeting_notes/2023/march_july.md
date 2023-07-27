# Matplotlib Weekly Meeting 

[![hackmd-github-sync-badge](https://hackmd.io/jd_7FjxNQ4y7XgNknvmvGQ/badge)](https://hackmd.io/jd_7FjxNQ4y7XgNknvmvGQ)

**A regular sync meeting for the project's maintainers, which is open to the community.** Everyone is welcome to attend and contribute to conversations.

## 9 March 2023 -- 20 July 2023


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
# 20 July 2023

## Agenda

### Old business

### New business

 - [x] RSE updates
 - [x] GSOC / GSOD updates
 - [x] scipy recap
 - [x] Kyle is 3.8 Release Manager
 - [x] New committer announcement
 - [x] 3.8 burn down
 - [x] GA is dead (well no longer collecting data)


## Notes

### RSE update
 - Kyle
     - scipy last week!
 - Tom
     - issue and PR review
     - 
### GSOC
- going well
- working on Open PR
    - adding middle delimiters
    - meeting on monday with Elliott

### GSOD
- draft of tagging guidelines exists
    - defining what is gallery vs example vs tutorial
- started working through simple PRs


### scipy recap
Elliott, Kyle, and Melissa attended

 - sprints in big room with numpy, scipy, matplotlib, scientific Python
     - code spaces documentation review from a new comer
     - talked with dependent libraries to make sure they are aware type hints are coming
     - more people than last year, 3 people with PRs
     - seemed like people had a better time getting started
         - codespaces helped with getting docs build on windows
 - presented on CZI grant
     - funding runs out on August 31
     - Melissa going back to being volunteer
 - had a Matplotlib tutorial
     - several people said it solved problems they had!
     - from back of room people seemed happy
 - array API presenetation + discussion
     - effort to standardize API for the zoo of array libraries
     - not clear how useful it will be to us
         - we have c-code that work on the CPU memory array pointer so not clear how much gpu capabilities would help
         - does not really help our "we take (almost) anything as input" problem
 - numpy 2.0 is coming
     - Kyle is tracking, should not be a big problem for us
     - numpy 1.25 drops the need for "oldest supported numpy"
 - faster c-python
     - not clear it will directly affect us
     - there may be some interesting issues coming from threading changes
         - no one has really thought about Python threading so we may discover global caches we did not realize was being protected by the GIL
     - lead by mbdoom (who gave a keynote)

### announcements
 - Kyle is 3.8 release manager
 - Scott Shambaugh has accepted commit rights

### GA is dead
- Melissa will reach out to scientific Python people to move to palusible

### 3.8 burn down
 - colorbrewer license
     - has an approved PR
 - pyparsing confilts
     - PR upstream in flight
 - contour aliased property issue
     - pro to keep: easy to add
     - con: different from everything else
     - not perfectly equivolent due to single bool vs list of bool
         - deal with by doing `all` on the way out, and up-casting on the way in
         - setter already support the broadcasting
     - currently no mixed `set_x` and attribute access in the wild because old version
       did not have getter/setters
     - *decision* : put in deprecated propery with `all` on the way out
 - intend to branch as soon as release critical issues are sorted
     - pyparsing depend on someone outside the project, proably the blocking issue
 - issues
     - https://github.com/matplotlib/matplotlib/pull/22347
         - decide to take it, but change to "system" instead of "auto"
         - leave as macos specific for now, if we broaden later deal with deconfliting then
     - 25966 

### New Business

# 13 July 2023
No meeting this week.

# 6 July 2023

## Agenda

_attending_: @QuLogic, @jklymak, @ksunden, @efiring, @devrd, @story645

### Old business

### New Business
 
- [x] RSE updates
- [x] GSoC and GSoD
- [x] 3.7.2 released
- [x] [name=QuLogic] SciPy Tools Plenary talk
- [x] [name=hannah] new note page 

### PRs and issues
- note ~~81~~ 75 actionable PRs.
- [ ] [name=anntzer] https://github.com/matplotlib/matplotlib/pull/14943 xkcd python style file

## Notes

### RSE
- @ksunden: travel and holidays
    - some 3.8 work.  3.7.2 out w/ @QuLogic 
    - pyparsing error message parsing working with upstream
    - scipy next week: tutorial  8 AM monday.  W-F main conference, S and Su, sprints. @QuLogic there as well
- @QuLogic 
    - 3.7.2 out
    - bumped 3.7.3 things
    - 3.8 review issues
- New contributor meeting
    - maybe needs advertisement

### GSoC GSoC
- @ratna: mathtext things
  - Working on open PRs
      - substack
      - LatinModern font support
- GSoD: holidays

### 3.7.2 released...
- No GPG signatures on PyPI - small affect on downstream developers.  We won't sign any more
    - not used on Fedora, for instance

### Scipy Tools plenary talk
- project over past year.  
- let @QuLogic if there are any highlights.
- <3 minutes, 2 slides
- there will be a repo for the talk..
- https://github.com/QuLogic/scipy2023-mpl-update

### New note page
- need to add one

### xkcd python style file
- https://github.com/matplotlib/matplotlib/pull/14943 
- python OK for style files at all?
- python configuration library?  restricted subset?
- import as normal python?
- exec instead of import...
- the PR refactors the seaborn styles for lack of repetition.
    - common file?
- cycler another issue
- 

---------------------
# 29 June 2023
## Agenda
_attending_: @rcomer, @devrd, @ksunden, @esibinga, @efiring, @melissawm, @tacaswell, @QuLogic, @story645, @ryliewei

### Old business

### New business

- [x] RSE updates
- [x] GSOC and GSOD updates
- [x] 3.7.2 release
- [ ] 3.8 burn down
- [x] [name=hannah] start new notes because of lag


### PRs

- Non-draft, 3.8 milestone: https://github.com/matplotlib/matplotlib/pulls?page=1&q=is%3Aopen+is%3Apr+milestone%3Av3.8.0+draft%3Afalse
- Location and rotation of offset text in 3D https://github.com/matplotlib/matplotlib/pull/26185
- [name=story645] [sketch seed](https://github.com/matplotlib/matplotlib/pull/26050)
    - [path randomness is repetative](https://github.com/matplotlib/matplotlib/issues/13479)
    - needs consensus: same artists diff or same in seed=arbitrary
## Notes

### RSE, GSOC, GSOD update
 - Caswell: time off last week, some review work
 - Kyle:
     - pyparsing investigation, need changes to upstream to unbreak our test
     - found a 25% improvement in parsing mathtext 
     - general review
 - Elliott
     - bit of documentation work
     - follow up on py312 fallout
     - mpl 3.8 burndown and backports for 3.7.2
 - Melissa
     - documentation (code spaces and proposal for re-org of dev docs)
 - Ratna
     - working on PRs
     - working on adding latin moden 
 - Eva
     - drafting tag hiegharchise
     - aiming for August 1 for docs on how to add new categories
     - working on defining example vs tutorial
 
### 3.7.2 
- all backports are created, but GHA was having issues last night
- a couple of still open PRs
    - https://github.com/matplotlib/matplotlib/pull/25960
## Pull Requsets    
### offset texts in 3D
- offset alignment in Z/X axis: 
  - baseline  of z is label is offset uncentered
  - x label rotates/anchor changes on rotation of figure
  decisions: 
  - orient relative to axis labels and center as specified in [3D offset example](https://matplotlib.org/stable/gallery/mplot3d/offset.html)
  - https://github.com/matplotlib/matplotlib/pull/26185 only needs to be squashed.

## 3.8 burndown
 
- most of critical are merged
- pcolor more meshlike still outstanding https://github.com/matplotlib/matplotlib/pull/25027
- subfigure_mosaic stil outstanding https://github.com/matplotlib/matplotlib/pull/26061

## random seed

- make sure typing is 3 or 4 tuple
- implementation: move seed management to python
    - make a private attribute on figure 
    - xkcd will get/set the rcparam seed
    - render manages the seed update/does the incrementing
    - reset the count on the renderer 
    
- add rcparams: 
    - sketch_seed: default 0 
    - iter_seed: bool, will implement on request
- add top of Figure.draw it should reset render._draw_count:
    
renderer = artist_seed if artist else rcparams
xkcd = set sketch_seed if seed else rcparam


---------------------
# 22 June 2023
## Agenda
_attending_: @oscargus @efiring @ksunden @QuLogic @greglucas @melissawm @devRD @evasibinga @story645 

### Old business
### New business
- [X] RSE updates
- [X] GSOC and GSOD updates
### PRs
- Non-draft, 3.8 milestone: https://github.com/matplotlib/matplotlib/pulls?page=1&q=is%3Aopen+is%3Apr+milestone%3Av3.8.0+draft%3Afalse
- [name=oscargus] Linestyle handing unification https://github.com/matplotlib/matplotlib/pull/23056
- [name=Melissa] Please test out [codespaces](https://docs.github.com/codespaces) if you are interested and give feedback/ask for more features if you notice anything :) 
- [name=oscargus] Performance improvements 
    - https://github.com/matplotlib/matplotlib/pull/26164
    - https://github.com/matplotlib/matplotlib/pull/26167
    - https://github.com/matplotlib/matplotlib/pull/26168 (not really performance but still a continuation)
    
## Notes

### RSE updates
- Kyle: Took a few days off this week, catching up afterwards
- Elliott: CI stuff, getting 3.12 working, checking Deprecations; some doc work, cleanup (e.g., images no longer in use)
- Melissa: got CodeSpaces working for mpl; embedded fluxbox desktop; ubuntu-based; available via button on github; some limits on computation usage. Note: does not automatically activate the conda environment. Try it; it is a work in progress. Requests for improvements have been submitted to CodeSpaces. [Tracking issue](https://github.com/matplotlib/matplotlib/issues/26169)

### GSoC / GSoD updates
- Ratna: looking at older issues; working on PR on subscript stacking (e.g. multiple conditions on a summation).
- Eva: gallery tagging: spreadsheet.  What tags make sense? Process for proposing new tags? Testing use of a GUI for image tagging.

### PRs
- [name=oscargus] Linestyle handing unification [#23056](https://github.com/matplotlib/matplotlib/pull/23056).
    - Suggestion: Add a "future warning"?
    - Example of a similar case suggested by Elliott.
        - [#12380](https://github.com/matplotlib/matplotlib/pull/12380) -> [#16474](https://github.com/matplotlib/matplotlib/pull/16474) -> [#23302](https://github.com/matplotlib/matplotlib/pull/23302)
        - https://github.com/matplotlib/matplotlib/pull/12380#issuecomment-426683961
    - Does [#24257](https://github.com/matplotlib/matplotlib/pull/24257) provide a similar model? Not exactly the same, because it involves a change in attribute behavior, not the type of a returned object.
    - Greg asked whether the use of a 2-cycle kwarg causes more pain than it relieves.
    - What is the usage case for get_linestyle? Seaborn uses it in bar https://github.com/search?q=get_linestyle%28%29&type=code
    - Possible solution: warn people to use "get_dashes" for collections.
- [name=oscargus] Performance improvements 
    - https://github.com/matplotlib/matplotlib/pull/26164 reduces unneeded calls to clear when Axes are created.
        - What to do about "register_axis" calls (spines dictionary)
    - https://github.com/matplotlib/matplotlib/pull/26167 (not controversial)
    - https://github.com/matplotlib/matplotlib/pull/26168 (not really performance but still a continuation)
    - Discussion about Ticking and optimizations: https://github.com/matplotlib/matplotlib/issues/5665
        - Need something like a text collection.
        - Also consider grid.

---------------------
# 15 June 2023
## Agenda
_attending_: @melissawm, @story645, @jklymak, @ksunden, @QuLogic, @tacaswell, @rcomer, @ianthomas23, @devRD, @greglucas, @efiring

### Old business
### New business

- [x] RSE updates
- [x] GSOC and GSOD updates
- [x] [name=tacaswell] stop building 32bit windows wheels [contourpy]
- [x] [name=QuLogic] also stop building `universal2` macOS wheels [#26125](https://github.com/matplotlib/matplotlib/pull/26125)
- [ ] [name=tacaswell] new contributor PRs
    - [ ] https://github.com/matplotlib/matplotlib/pull/25839
    - [ ] https://github.com/matplotlib/matplotlib/pull/22761
    - [ ] If any maintainers have time, please take a look at the "Needs review" (and the "Needs decision") column on https://github.com/orgs/matplotlib/projects/1/views/3
- [x] [name=tacaswell] 3.8 burn down
- [x] [name=tacaswell] progress on image test overhaul

### PRs
- [x] [name=hannah] [python 3 setup note](https://github.com/matplotlib/matplotlib/pull/26084)
- [x] [name=greglucas] pcolor more meshlike https://github.com/matplotlib/matplotlib/pull/25027
- [x] [name=greglucas] Contour rework merge? https://github.com/matplotlib/matplotlib/pull/25247 Was holding off for baseline image work

## Notes

### RSE updates
 - kyle: scipy tutorial prep; current on personal account, will move to mpl when done.  Lots of issue review.  
     - sprints at scipy? Maybe to mentored sprints
     - July 15 and 16
     - using notebooks/ipympl for tutorial
 - Tom: baseline imaging progress.  Reviews
 - Melissa: travelling; codespaces setup (versus local dev)
 - Elliott: CI work - ARM build; Meson work; newer versions of TexLive etc. Update windows install instructions.
- Ratna (GSOC): Older mathtext issues and PRs
- GSOD: making progress 

### Win32 and ARM universal2 wheel builds:
- stop win32? 
- cpython has 32bit builds
- numpy/scipy don't have 32 bit wheeels.
- pypy stats hard to believe (most CI)
- ARM universal2
    - already ship individual (ARM and Intel)
    - universal installers can fuse them anyways if they need to
    - numpy doesn't have these wheels

### 3.8 burndown
- keep working on it?
- RC 30 June - what _needs_ to go in?
- rcParams update?
    - dict subclass
- image tests may be optimistic...
    - might make backporting a pain
    - image tests may not be backported.
    - 
- push rcparams work to 3.9
    - do not do this under pressure
    - gives a chance to extend it over time
    - rcparams have historically been brittle, we should make sure we dog-food this.
- get subfigure_mosaic landed
    - new ish contributor, waiting on tests
- pcolor->more mesh like
    - pcolor more meshlike https://github.com/matplotlib/matplotlib/pull/25027
    - downstream broken?
    - needs more API notes 
- contour updates https://github.com/matplotlib/matplotlib/pull/25247/files
    - good idea, should go in
    - needs better API notes

### Test images
- lots of progress
- command line interface to help with managing files or caches
- touch base with pytest-mpl
- 

-----------
# 8 June 2023
@attendance: @efiring, @z5VMbcx5SRm9Et4RWXmJrA chahakmehta, @devRD(ratna), @greglucas, @ksunden, @brianholland, @ksunden, @qulogic, @tacaswell, @story645, @anntzer

## Agenda

### Old business
### New Business
 - [x] RSE updates
 - [x] GSOC and GSOD updates

### Issues and PRs
  - [x] namespace package issue https://github.com/matplotlib/matplotlib/pull/25381/files
  - [x] bold symbol PR https://github.com/matplotlib/matplotlib/pull/25661


## Notes
 - RSE updates
     - caswell: not as much as I want, but mostly issues
     - Kyle: dev docs on how to handle typehints + deprecations, started work on scipy tutorial (need to push to github), data prototype work
     - Elliott: fixed website.  We have alerts, but they did not fire.  Looking into making webhooks error.  Working on older PRs (PDF images, re-viving arm testing, moving to pyproject.toml (in prep of move to meson))
 - GSOD
     - Eva spent the week getting sphinx tagging working and getting setup for development
     - should see public work in the next few weeks
 - GSOC
     - kick off meeting on Monday
     - starting to prioritize issue
     - working on Open PRs
     - starting to look at accent and positioning

### namespace packages
 - https://github.com/matplotlib/matplotlib/pull/25381
 - name space packages need to have character-for-character identical __init__.py
 - wheels have been stripping these for a while
 - develwheel on widows has been putting (a different version) back
 
 
 *decision*
 
 - merge the mpl PR
 - @ksunden will put a PR into basemap to bring thing in line too

### pyproject.toml move
- requires everything to be declarative
- we have a bunch of non-declarative stuff in our setup.py
 - only require setuptools_scm when in a git repo
     - may not be a way to do this auto-magically
     - maybe move into [dev] 
         - and add pytest, change install instructions for dev to target `.[dev]`
 - provide options to build against system freetype / qhull
     - can probably handle that in the build process
 - should we ship the test images or not in the wheels
     - can do this with meson

*decision*

 - @QuLogic will take over this PR and merge with meson work

### mouse over on twinned axes

https://github.com/matplotlib/matplotlib/pull/25556

discussion is over how to format

criteria:
 - not too much width
 - be very clear to the mind

preference to last version in https://github.com/matplotlib/matplotlib/pull/25556#discussion_r122297156 of

x, y = (1, 2) | (2, 3)

discussion about if we should change the non-twinned axes to also be 

x, y = (1, 2)



# 1 June 2023
@attendance: @ksunden, @jklymak, @QuLogic, @efiring, Haoying Zhang (@stevezhang1999), @melissawm, @oscargus, Ratna(@devRD), @rcomer, @tacaswell, @story645 

## Agenda

### Old business
    
### New business

 - [x] RSE updates
 - [x] GSOC and GSOD updates
 - [x] [name=tacaswell] 3.8.0 release schedule
 
### Issues and PRs
 - [x] [name=oscargus] [Data cursor](https://github.com/matplotlib/matplotlib/issues/9957) - should make a decision, not just let it become inactive.
     - [Data tooltip](https://github.com/matplotlib/matplotlib/issues/23378) is a related approach that may be worth considering in the discussion. ([Related PR](https://github.com/matplotlib/matplotlib/pull/25831)) 
 - [x] [name=tacaswell] slimming down (or expanding) subpackage imports https://github.com/matplotlib/matplotlib/pull/26017
 - [ ] [name=jklymak] Issue expiry? https://github.com/matplotlib/matplotlib/pull/25938

## Notes

### RSEs

- @ksunden: At scipy maintenrs confab in Seattle.  meeseeksbot being renamed to "lumberbot" (maybe). Nightly wheel location being cleaned up.
    - units infrastructure, units dtype in numpy. With sebastien. 
    - Catching up
- @QuLogic: Old PR work.  Meson work ready.  Some CI issues broken last week fixed.
- @tacaswell: issue review; Breaking SciPy doc builds on multiple cores on a Mac.
- @melissawm: Old PRs that haven't been getting through.  New contributor meeting Tuesday 1300-1400 EDT.  Melissa can't do it - can anyone help?  @tacaswell and @story645 can help.

### GSOD:
- prototype of tagging.  Draft of guidelines by end of summer.
- tagging 70%.

### GSOC:
- @Ratna: operater in Mathtext.  Relational operators, and new ones.  @kyle and @QuLogic mentoring.  @oscargus working on similar things.  Prioritization? 
- Maybe page to track the project?  Mayeb GitHib Project
- just started this week.

### 3.8 release
- July
- issues that might block
    - Image testing overhaul
    - type hints in docs.
    - user explain / top level re-org
- RC last week June, release middle/end July
    - before SciPy (at least RC)
- New features:
    - type hints
    - ECDF, figure titles, math things.
    - a lot of API changes

### Data Cursor:
 - [Data cursor](https://github.com/matplotlib/matplotlib/issues/9957) - should make a decision, not just let it become inactive.
 - [Data tooltip]
 - Example of issue that expired.
 - mplcursors exists; should stay thirdparty?
     - native better?
     - hover and click
 - Native tooltips...
     - https://github.com/matplotlib/matplotlib/pull/23378
     - tooltips themselves generally useful, which we don't have.
 - Hover events?
     - https://github.com/matplotlib/matplotlib/pull/25831
     - probably don't want hover events.
 - Conclusion:
     - #25831 probably discouraged (@tacaswell will comment)
     - #23378 tooltips support needed
     - #9957 close and not accept

### importing `matplotlib`
- trying to strip things that don't need to be there.
- https://github.com/matplotlib/matplotlib/pull/26017
- very small import time difference.
- SciPy is discussing lazy module importing
- maybe import `matplotlib.figure` by default
    - you need `Figure` to do what it is we think it is you do with Matplotlib
- conclusion:
    - close PR
    - leave expanding it as food for thought

### Speed of expiry bot

- go faster or go slower
    - keep same for now?
    - should label more as "keep" actively.


---------------------
# 25 May 2023
@attendance: 

## Agenda

### Old business
- [x] [name=story645] gitter to matrix: 
    - spaces is the [official replacement](https://github.com/vector-im/roadmap/issues/26)
    - spaces based authentication is a [WIP spec](https://github.com/matrix-org/matrix-spec-proposals/pull/2962)
    - proposal: use spaces w/ manual registration until features are implemented
    - activity side panel is [stalled pr](https://github.com/matrix-org/matrix-hookshot/issues/631) on matrix-hookshot (used for bridging)
    
### New business

 - [x] RSE updates
 - [x] GSOC and GSOD updates
 - [x] @kolibril13 Short Matplotlib demo

### Issues and PRs
- [x] [name=story645] [plot types - user guide - tutorials - examples - reference](https://github.com/matplotlib/mpl-sphinx-theme/pull/72) - overview to details 
- [x] [name=tacaswell] how to document transXYZ attributes https://github.com/matplotlib/matplotlib/pull/25922

## Notes

### RSE updates
- @tacaswell, some PR review
- @QuLogic meson work, working on windows issues, older orphaned PRs - reduce PR count.
- @Ratna: GSOC relational operator, PRs waiting on review...
    - PR: https://github.com/matplotlib/matplotlib/pull/25933
- GSOD: Met w/ Eva - making spreadsheet, working on timeline; some permission issues.
    - work log: https://hackmd.io/uiu3amD3SpOFrGyFUOK07Q

### Demo
- incorporate tldraw into Matplotlib https://github.com/kolibril13/jupyter-tldraw/tree/ff285974174189f34545be50f5dc71eb41302cb7/future_ideas/annotate_matplotlib
- demo of gallery searcher that narrows down the thumbnails to just those that have searchterms
https://discourse.matplotlib.org/t/the-matplotlib-gallery-with-dynamic-search/23826?u=kolibril13

### Gitter
- "spaces" replacement for setting permissions on rooms
    - no linked authentication
    - add new folks
- sidebar with status stalled PR
- pr on comms guide that mod access is by request

### Navbars:
- dev->contribute
- do it!

### rename exmaples
- rename 
- re-directs
    - need to add stable/gallery -> stable/examples 301 when we publish

### transAxes/transData etc
- not documented on the objects
- https://github.com/matplotlib/matplotlib/pull/25922
- Options:
    - class variable: defaults None w/ docstring
        - type unstable
        - maybe use identity transfrom an default, but could lead to other confusing behivor
    - properties
        - better for interactive query
        - can make read-only (though we may mutate internally)
        - slower than attribute look up
    - add to docstring
        - risk getting out of sync
        - more manual query
    - class variable with just type
        - but would start to leak typing information into the code
- make properties snake case (some of the only places that use camel case)
    - have talked about this before but decided too much work


Consenus
 - go with properties
     - but do coarse bench marks to see if it matters
 - option to look at read-only
     - would need a deprecation cycle
     - check how disruptive this would be
 - consider renaming
     - https://github.com/matplotlib/matplotlib/pull/11051 is prior art
 - the docstrings are not yet clear
     - need to be more explicit about source and target coordinate systems
     - link to transform tutorial

------------------------------
# 18 May 2023
@attendance:  @kyle, @tacaswell, @efiring, @story645 , @melissawm, @Eva Sibinga, @Haoying Zhang, @Chahak Mehta. @Ratna, @ianthomas23
## Agenda

### Old business
 - [x] [name=tacaswell] update on image testing overhaul
 - [ ] [name=elliott] update on leak finding

### New business
 - [x] RSE updates
 - [x] GSOC and GSOD updates
 - [x] [name=story645] adding outside collaborators
 - [x] [name=story645] general purpose docs gitter/matrix channel
 - [x] [name=story645] github-matrix bridging
 - [x] [name=melissawm] GSoD Update: Technical writer hiring in progress :tada:
 - [x] [casting to numpy]( https://github.com/matplotlib/matplotlib/issues/25882#issuecomment-1553480984)
 - [x] [name=mellissa] explaination pages moving

### Issues and PRs
- [x] [name=story645] nav bar changes:
     - [x] [develop->contribute](https://github.com/matplotlib/mpl-sphinx-theme/pull/71) - it was contribute first & not all contributions are code
     - [x] [plot types - user guide - tutorials - examples - reference](https://github.com/matplotlib/mpl-sphinx-theme/pull/72) - overview to details 

## Notes

### RSE and GSOC and GSoD:
- @ksunden SciPy summit.  Data prototype work, issue review
- @tacaswell, image testing, admin, PR review etc
- @melissawm: doc issues.  Inter-project working groups/culture labs (more info here: https://discourse.matplotlib.org/t/fostering-an-inclusive-culture-call-for-participation/23783)
- @ratna: GSOC: relation operators, some spinup meetings
    - mathtext set of issues...
- @eva: starting next week with @melissawm and @story645
    - indexing gallery examples and information architecture...

### Adding outside collaborators
- matplotlib-steering-council@numfocus.org
    
### Gitter
- Currently no bridging between github and matrix/gitter
- new channel for docs?
- repurpose GSoD? or community?
- ask for incubator adds on the community channel?

### Casting to numpy
- frequently hit issues where we have issue
    - people try to pass us "array like thing"
    - sometimes crashes
    - in this case slow
- do we have a good documentation of exactly what we take
    - push this up the Kyle's TODO list for 2 weeks
- xarray has ability to carry units as meta-data, but not programatically used
- numpy's new dtypes can in theory carry physical units

### Moving example pages
- long discussion about what the right organization of the user guide is
- old organization had bad
    - conceptual grouping
    - depth of details grouping
- we should add a new "archiceture" top-level in the user guide 
    - move API and backend here
    - put new short-versionof arch of open source software blurb (Mellissa is working on)
- maybe consider tagging these like examples
- should stay in users not dev because they really are for users not just for mpl devs

--------------
# 11 May 2023

## Agenda

### Old business
 - [x] [name=story645] in process of hiring GSOD writer [Eva](https://discourse.matplotlib.org/t/gsod-writer-hired/23796) 
 - [x] [name=story645] announce GSOD and GSOC hiring? on homepage
  
### New business
- [x] RSE updates

### Issues and PRs

- [x] [name=@greglucas] Contourset as a single LineCollection/PatchCollection [25247](https://github.com/matplotlib/matplotlib/pull/25247)
    - ~2 MB in image changes associated with this. Needs Mypy help. https://github.com/matplotlib/matplotlib/pull/25247#issuecomment-1537842858
- [x] [name=@oscargus] [Shadow and pie shadow](https://github.com/matplotlib/matplotlib/pull/25389)
    - Also makes sense to merge the above before [#24666](https://github.com/matplotlib/matplotlib/pull/24666) (I can fix that if the author is not up for it)
- [x] [name=@greglucas] Memory leak testing [25853](https://github.com/matplotlib/matplotlib/pull/25853#pullrequestreview-1421626522). We currently check memory thresholds, but do we want to ensure objects aren't in the list of gc.get_objects() using objgraph as an optional test dependency on one of the runners?
- [ ] [name=@oscargus] [Minimum QT version](https://github.com/matplotlib/matplotlib/pull/25363)
- [x] [name=@chahak13] What is the usecase for `rcdefaults`? Is the idea to go back to the default "style" values or the values present in `matplotlibrc`? If I'm reading it right, `rcdefaults` is almost entirely wrong. [Link](https://github.com/matplotlib/matplotlib/blob/8faa835c81d9cf12342992521ddb95e9a645bc36/lib/matplotlib/__init__.py#L1068-L1091)
- [x] [name=@chahak13] Scaling markers in scatter. Needs review https://github.com/matplotlib/matplotlib/pull/25259

## Notes

### introductions 
### gsoc project
 - mathtext improvements
 - improved latex integrations
 - mentors are Kyle and Elliott

### gsoc/gsod
 - we should put on web page
 - @kyle will do GSOC
 - @story645 or @melissawm please do GSOD

### RSE updates
 - Caswell
     - vacation / busy with BNL
     - engaging with upstream packgaing discussion
 - Kyle
     - general issue review
     - started GSOC meetings
     - attended packaging round table
     - thinking about data-prototype
 - Elliott
     - still fighting with laptop
     - orphaned PRs

### Issues
#### contour changes
 - [25247](https://github.com/matplotlib/matplotlib/pull/25247)
 - massively speeds things
 - changes a lot of test images (2M)
 - hold off for ~a month~ two weeks?
     - to give @tacaswell a chance to finish the image update work
 - also requried for fixing alpha in contours in pdf

#### shadow + pie
 - seems reasonable, just needs review (gone idle)
 - the linked PR should make use of new functionality for legend shadow

#### mememory leak

- had a number of bugs where we have long-lived cyclic references
- should we add tests to look for memory "leaks"?
- we do have ASV still sort of set up
    - could set up a memory-based benchmarks
    - but this also requires getting it setup again and running
- could do something like what we do for the callback stack leakage?
    - Elliott will look at
- https://www.fugue.co/blog/diagnosing-and-fixing-memory-leaks-in-python.html
- https://pypi.org/project/pytest-leaks/

#### rcparams discussion
- `clear` is no op and should be replaced by resetting to defaults function

#### GSOD
- put on next week agenda making a gitter channel for documentation
- communicate public work and update plan

#### 

# 04 May 2023

## Agenda

### Old business

### New business
 - [x] RSE updates
 - [x] [name=tacaswell] broken pypy39 wheels https://github.com/matplotlib/matplotlib/issues/25811
 - [x] GSOD
 - [x] GSOC

## Notes

### GSOC
 - we were accepted for GSOC with the Math Text proposal by devRD (just posted!)

### GSOD
 - currently doing interviews, part of the way through interview pool, should decide by Sat
 - deadline to hire is May 10 (need to identify person and tell Google, not have contracts signed)
 - working with NF to set up the IC contracts, money will come through open collective

### RSE updates
 - Caswell
     - PR to CPython for input issue
     - example PR for new image scheme
     - PR review
 - Kyle
     - general issue / PR review
     - tracking down fallout from numpy changing sin/cos computatitons
         - single LUP changes broke 3 tests
         - PR just open
     - work on validating converters and formatters
         
 - Elliott
     - laptop drive died, lost a bit of work + time
     - stale bugs triage
     - work on images
     - bit of work on confusing PDF compression bug
 - Melissa
     - GSOD
     - as part of grant, worked with DEI consultant who wrote a report
         - report is now public, will put as news item on our home page
         - starting Culture Labs

### pull pypy39 wheels

- 
- https://github.com/numpy/numpy/pull/23528 may be related
- *we will yank the pypy39 wheel*
- won't remove from CI, just note to not upload


### image externalization work

- (described)
- 


# 27 Apr 2023

## Agenda

### Old business
- [ ] GSOD 

### New Business
 - [x] RSE reports (Weekly worklog not used?)
 - [x] [name=tacaswell] pypi organization for mpl ? https://matrix.to/#/!BXmyZMTnRjWJldDRLV:gitter.im/$MJFPkcAmG4UHgOKC0dqpXCkVBm7EG4V-ihNHyh-2MMc?via=gitter.im&via=matrix.org&via=aria-net.org (brought up on gitter by @dopplershift )
 - [x] [name=oscargus] Should there be unused imports in the stub files? Example: `FT2Image` in `mathtext.pyi`
 - [x] [name=oscargus] PS vs. EPS. Is PS still needed (basically PS expects a paper size, which is buggy, and most users probably expects a properly sized figure anyway)?
 - [x] [name=QuLogic] Removing travis
 - [x] [name=QuLogic] server-side redirects: mpl-third-party and examples
 - [x] [name=story645] GSOD - closing applications and making short list tomorrow?- anyone want to participate in writer selection?
 - [x] [name=story645] registering for an account on bluesky to squat name/general policy for registering accounts

### Issues and PRs
- [ ] [Draw 3D gridlines below axis lines, labels, text, and ticks](https://github.com/matplotlib/matplotlib/pull/25482) Very likely to end up in rebase limbo.
- [x] [name=@chahak13] Added performance impact of using ChainMap for RcParams in description. ([#25617](https://github.com/matplotlib/matplotlib/pull/25617))
- Bump list (probably nothing to discuss)
   - [shadow and pie shadow](https://github.com/matplotlib/matplotlib/pull/25389)
   - [sketch pathcollection](https://github.com/matplotlib/matplotlib/pull/25645) - should it wait on implementing seed setting parameter, which has a proposed patch
   - [minimum Qt5 version for mpl 3.8](https://github.com/matplotlib/matplotlib/pull/25363)
   
   
## Notes

### RSE updates
 - Kyle:
     - normal issue / PR work
     - 2 versions of code validate formatters / converters, may need new API
 - Tom
     - nerd-snipped into fixing a CPython bug
     - general issue / PR review
 - Elliott 
     - continued work on post script
     - resolved most of the PS bugs that are not spcefic to the PS format
     - continued work on DPI refactor
         - might be able to generalize the DPI handling across vector backends
             - but we have a lot of hard-coded 72s in the backends
             - tests seem to run, but worry about lots of edge cases
             - not clear we really want / need to do this, but it is working
             - might help with the pdf/ps issues with shifted lines and colorbars
         - @jklymak is also working on the shifted (low-dpi) rasterized embeds in vector backends at low DPI
             - part of the problem is that because there is a stroke on the border, the rasterize includes this boarder, but the computed bbox does not
             - may need "true bounding box"
 - worklog stopped being filled in, we should start doing this again
    - https://hackmd.io/@matplotlib/HyVoUHlSo
    -
### Pypi org
- pypi now has organizations
    - still not a lot of information
    - free for community projects, use to generate revenue
    - consolidate our packages into one org
    - expectation is that teams will lets us do better ACL
- do we want to ask for an org?
    - go our own or a community wide one?
- decision: lets go ahead and get one @dopplershift will do


### unused imports in stub files
- multiple levels of imports in stub files
    - everything in .py file + what is needed to do type
    - just what you need
    - not a clear community standard
- what (re)-imported things are considered part of the public API
- mympy only considerd things imports via `import Foo as Foo` to be publically exported
- may have to be case-by-case
    - but in this case it should be removed

### PS versus EPS
- papersize: 
    - https://github.com/matplotlib/matplotlib/issues/7551 
        - automatic size picking does not quite work
        - always picks something in the b-series
        - b10 is near b1 not b9 so never get b10
    - do we actually _need_ paper size?
        - we set the paper size, place the figure in the middle, and then crop to the figure
        - if user specified a paper size respect, but drop "auto" behavior
        - @oscargus notes PS needs a paper size, but @QuLogic 's understanding of the spec is that we do not
            - think it is only used for media selection when sending straight to a printer
- propsoals
    - deprecate the "auto" functionality
    - default is currently "letter", switch to making the figure just the right size
        - concerns
            - people who are making PS _may_ be sending them straight to printers!
    - deprecate the whole thing?
        - basically the same code as eps so cost of keeping around is low
        - slightly diffrent header / footer than eps
        - can we get better results via pdf -> external distiller to eps
            - some cases where it does not work perfectly (related to hatching)
            - what does pdf -> eps via distiller do with transparency?
            - 
**decision**

deprecate auto, punt on the rest

### Travis

notification: has been turned off for a year, will remove

### server side re-directs

- proposal:
    - put in a server side re-direct to matplotlib.org/third-party from matplotlib/mpl-third-party to reduce redundency
    - name needs some discussion
        - used to be thirdpartypackages
        - currently https://matplotlib.org/mpl-third-party/
        - 3pp is a propsoal
            - discussion of getting really short re-directs 
    - decided on going back to thirdpartypackage

- issues with gallery / examples naming
    - examples get served under matplotlib.org/stable/gallery but come from gallery/examples
    - propsoal:
        - change where they are written to to matplotlib.org/stable/examples
        - add server side re-direct from gallary -> examples
        - probably want to keep the re-direct forever (but use 30-permenent redirect)
        - configuration is in https://github.com/matplotlib/matplotlib.org


### GSOD
- got a lot of propsols, enough good candidates
- plan to short list tomorrow
    - if you want to be involved ping @story645 and @melissawm 
- google wants writer hired by May 10
- project is about cataloging existing content not writing new content
    - index gallery and develop tagging scheme
    - write developer docs on how to tag new things in the future, how to add new tags

### do we want to register on new platforms?

- bluesky 
    - do it!

----------------   
# 20 Apr 2023

```
2023-04-20 19:00:00+00:00
Europe/Berlin        2023-04-06 21:00:00+02:00
UTC                  2023-04-06 19:00:00+00:00
America/New_York     2023-04-06 15:00:00-04:00
America/Vancouver    2023-04-06 12:00:00-07:00
US/Hawaii            2023-04-06 09:00:00-10:00
```

## Agenda

Attending: @tacaswell @story645 @QWhXj01mSwmTjk5kN1H_qQ @jklymak @pXw4hSgTQF2--OciPYwa1w @melissawm @oscargus @devrd @chahak @ksunden @QuLogic 

### Old Business
 
### New Business

- [x] RSE reports
- [x] GHC day https://app.sessionboard.com/submit/grace-hopper-celebration-2023/f9ed4ea9-3e3e-4936-a112-c4f4af24dbfc need to submit by 4/26
    - need 3 people willing to have their name + email listed as mentors
- [x] [name=oscargus] Add automatic comment on "Good first issue" with appropriate links to guidelines etc? https://github.com/marketplace/actions/create-or-update-comment https://docs.github.com/en/actions/managing-issues-and-pull-requests/commenting-on-an-issue-when-a-label-is-added
- [x] website TLS issues

### Issues and PRs

- [x] https://github.com/matplotlib/matplotlib/pull/25515 srcset for plot_directive.
- [x] [name=oscargus] [#25642](https://github.com/matplotlib/matplotlib/pull/25642) opinions before adding tests and documentation (or closing)?
- [ ] [name=oscargus] artist property keyword argument documentation incl. rcParams [Option 1](https://github.com/matplotlib/matplotlib/pull/22699), [Option 2](https://github.com/matplotlib/matplotlib/pull/22749), [Option 3 (only a suggestion, can be combined with others)](https://github.com/matplotlib/matplotlib/issues/25644)
- [x] [Figure repr](https://github.com/matplotlib/matplotlib/issues/9372) This should be closed I believe
- [x] [extended wilkinson method for tick locators](https://github.com/matplotlib/matplotlib/issues/9373) still intended?
- Bump list (probably nothing to discuss)
   - [shadow and pie shadow](https://github.com/matplotlib/matplotlib/pull/25389)
   - [sketch pathcollection](https://github.com/matplotlib/matplotlib/pull/25645)
   - [mathbfit mathtext command](https://github.com/matplotlib/matplotlib/pull/25359)
   - [minimum Qt5 version for mpl 3.8](https://github.com/matplotlib/matplotlib/pull/25363)
   - [Draw 3D gridlines below axis lines, labels, text, and ticks](https://github.com/matplotlib/matplotlib/pull/25482)

## Notes

### RSE updates
- @tacaswell: Image set work, PR..
    - [PR](https://github.com/matplotlib/matplotlib/pull/25734) now open.  Look at and discuss next week
    - https://github.com/tacaswell/mpl-imageset-demo
- @ksunden
    - PR review etc.
    - data prototype work
    - GSoC work
    - typing in down-stream libraries
- @melissawm 
    - travel
    - SGoD proposals ongoing; good candidates
- @QuLogic
    - hiDPI work
    - postscript work

### Grace Hopper
- due 26 April: 3 names/addresses

### Scipy tutorial
- accepted for tutorial (July)
- perhaps seek input

### Good First Issue
- maybe add bot to add a comment to good first issue pointing to devdocs
- should be possible with current workflows
- method to better screen
    - try to add short justification for why good first issue
- add info to PR template to make sure people link..
- communicating crossed PRs

### Website
- @QuLogic is fixing manually

### [srcset for plot_directive](https://github.com/matplotlib/matplotlib/pull/25515).
- needs review

### [rcParams for 3d](https://github.com/matplotlib/matplotlib/pull/25642)
- general idea

### decorator for kwargs that have rcParams
- decorators for every function
- versus parsing the docstring of the setter/getter?

### Wilkinson ticks
* maybe want, needs to be prototyped and evaluated, possibly as an external library 



---------------------
# 13 Apr 2023

```
2023-04-13 19:00:00+00:00
Europe/Berlin        2023-04-06 21:00:00+02:00
UTC                  2023-04-06 19:00:00+00:00
America/New_York     2023-04-06 15:00:00-04:00
America/Vancouver    2023-04-06 12:00:00-07:00
US/Hawaii            2023-04-06 09:00:00-10:00
```

@jklymak @chahak @ksunden @oscargus @melissawm @QWhXj01mSwmTjk5kN1H_qQ @timhoffm @tacaswell @QuLogic 

## Agenda

### Old Business
 
### New Business

- [x] RSE reports
- [x] GHC day https://app.sessionboard.com/submit/grace-hopper-celebration-2023/f9ed4ea9-3e3e-4936-a112-c4f4af24dbfc need to submit by 4/26
- [x] [name=Melissa] Docs on codespaces? https://github.com/matplotlib/matplotlib/issues/25398
    - May be very useful for sprints!

### Issues and PRs

- [x] [name=QuLogic] [name=oscargus] eventplot corner cases [#22286](https://github.com/matplotlib/matplotlib/pull/22286)
- [x] https://github.com/matplotlib/matplotlib/pull/25617 RcParams->ChainMap
- [ ] https://github.com/matplotlib/matplotlib/pull/25515 srcset for plot_directive.
- [ ] [name=oscargus] [#25642](https://github.com/matplotlib/matplotlib/pull/25642) opinions before adding tests and documentation (or closing)?
- [ ] [name=oscargus] artist property keyword argument documentation incl. rcParams [Option 1](https://github.com/matplotlib/matplotlib/pull/22699), [Option 2](https://github.com/matplotlib/matplotlib/pull/22749), [Option 3 (only a suggestion, can be combined with others)](https://github.com/matplotlib/matplotlib/issues/25644)
- [x] [name=jklymak] [bar/barh units meaning of height/width](https://github.com/matplotlib/matplotlib/pull/25667)
    - eg does `bar([0, 1, 2], height=['cat', 'dog', 'cat'])` really get used, and why? 
- Bump list (probably nothing to discuss)
   - [shadow and pie shadow](https://github.com/matplotlib/matplotlib/pull/25389)
   - [sketch pathcollection](https://github.com/matplotlib/matplotlib/pull/25645)
   - [mathbfit mathtext command](https://github.com/matplotlib/matplotlib/pull/25359)
   - [minimum Qt5 version for mpl 3.8](https://github.com/matplotlib/matplotlib/pull/25363)
   - [Draw 3D gridlines below axis lines, labels, text, and ticks](https://github.com/matplotlib/matplotlib/pull/25482)
- [x] [name=Melissa] CircleCI token fix https://github.com/matplotlib/matplotlib/pull/25672
    - Maybe related? https://app.circleci.com/pipelines/github/matplotlib/matplotlib/23508
## Notes

### RSE updates
- @tacaswell more thinking about test image overhaul.
    - text file gets made with list of files:
        - filename version timestamp 
        - this will show up in the commit with git/blame
        - SHA has issues with rebasing etc...
            - images not hash-stable in general (have metadata)
    - can get candidates for images that  with or will not work.
    - will have a test repo
- @ksunden:
    - typing issues
    - type checkers over dependencies (xarray, seaborn, plotnine)  some errors on our end to fix.
        - pandas: makes hard to check, no type hints plotting routines
    - CI issues
        - nbconvert, still buggy - PR on the way
        - mypy moves fast - bug filed - pinned mypy
    - GSOC: reviewd apps.  Elliott and Kyle have two or three likely candidates.
        - mathtext, bivariate colornorm
    - data prototype work: 
        - Expanding Patch support
    - Validating formatters/converter compatibility [#25662](https://github.com/matplotlib/matplotlib/pull/25662)
- @melissawm 
    - GSoD: feedback and information
    - CircleCI token update
        - other repos may need this too
    - codecov removed on Circle
    - Codespaces?
        - how-to in our docs? 
        - vscode on browser...
            - docker image pre-set dev environment
            - but docker sunsetting?
            - numpy/scipy decided to drop it
        - useful for sprints
        - need a json file for the environment
        - xvfb for seeing figures...
        - hard to get interactive figures in vscode
        - @melissawm will see if there is any way to create windows and other blockers.
        - how ephemeral?  Can save multiple sessions.  30 days persistence.
- @QuLogic 
    - CI fixing, GSoC, typing
    - Azure failing tk broken. Reported...
    - old issue review and PRs

### Grace Hopper 
- 26 April: sprint
- increase test coverage - largely checking datetime64 

### Event plot corner cases

- https://github.com/matplotlib/matplotlib/pull/22286

### rcParams: ChainMap
- https://github.com/matplotlib/matplotlib/pull/25617 
- better protection of rcParam global
- defaults stored in base layer
- contexts more elegant
- need to check performance of ChainMap versus dict.
- some top-level names that don't get a sub namespace.
- introduces new API, but ideally back compatible
    - maybe new API into a different PR?
- 3.7 we already had deprecators for `dict.__set_item__`.
    - so 3.9 would be target if we followed this deprecation.
    - but no one knows because we can't warn on it
    - maybe not really public API
- 

---------------------
# 6 Apr 2023

```
2023-04-06 19:00:00+00:00
Europe/Berlin        2023-04-06 21:00:00+02:00
UTC                  2023-04-06 19:00:00+00:00
America/New_York     2023-04-06 15:00:00-04:00
America/Vancouver    2023-04-06 12:00:00-07:00
US/Hawaii            2023-04-06 09:00:00-10:00
```

## Agenda

### Old Business
 
### New Business

- [ ] RSE reports

### Issues and PRs

- [x] [name=QuLogic] [Enable pre-commit for mpl-third-party?](https://github.com/matplotlib/mpl-third-party/pull/152)
- [x] [name=QuLogic] [mpl-sphinx-theme license?](https://github.com/matplotlib/mpl-sphinx-theme/issues/29)
- [ ] [name=QuLogic] [name=oscargus] eventplot corner cases [#22286](https://github.com/matplotlib/matplotlib/pull/22286)
- [ ] https://github.com/matplotlib/matplotlib/pull/25617
- [ ] https://github.com/matplotlib/matplotlib/pull/25515

## Notes

### Discussion of animitaion and figure sizing

- using the transform + figure resize to expand figure without moving things
    - scale the figure transform so that the top-right is no longer (1, 1)
- stick with being strict

### how to manage user confusion between us and downstream


### RSE updates
 - kyle
     - follow ups to typing PR
         - small detailed things
     - new contributor meeting
         - the align titles PR was discussed (#25591: https://github.com/matplotlib/matplotlib/pull/25591)
     - gsoc management
     - Investigate/address dependencies that broke our tests
        - Pyside6 requires libxcb-cursor0
        - nbconvert release changed file names
 - elliott
     - meson and documentation work
     - reviewing the typing PRs
 - tom
     - https://github.com/matplotlib/matplotlib/issues/25608
     - animation issue review
     - ban just on streaming ffmpegs?
     - just at grab-frame level
     - GSoD
- melissa
    - redirect GSoD stuff to a google group
    - a lot of interest in GSoD

### mpl-sphinx-theme
- License says BSD, but should be PSF..
- pytoml one place for license
- Should use a general license like BSD
- @QuLogic to add PR to fix

### pre-commit mpl-third-party
- recent style fixes, yaml-lint and json-schema
- enable pre-commit to check those.
- seems that yes!

### eventplot corner cases
- [#22286](https://github.com/matplotlib/matplotlib/pull/22286)
- Wait for @oscargus 

### markersize PR
- needs rebase, but should be good...

### rcParams
- [#25617](https://github.com/matplotlib/matplotlib/pull/25617)
- remove dict inheritence replace w/ ChainMapping...
    - defautls temporarily replaced by user values in context, 
    - we use dict getters and setters for rcParams.  
    - want namespacing to work, adding to dict, its getting pretty complicated. 
        - iterator, `in` are hard to get right.  Mostly like an dictionary, but...
    - don't need rcDefault anymore.
    - chain mapping allows undo one level deep or saved points.
        - makes context managers easier
        - default saved in chainmap
    - pros:
        - code simplified
        - name-space access rcParams['text'] - can get keys w/o prefix
        - need documenting and lay it out clearly because will be public API.
        - 


---------------------
# 30 Mar 2023

```
2023-03-30 19:00:00+00:00
Europe/Berlin        2023-03-30 21:00:00+02:00
UTC                  2023-03-30 19:00:00+00:00
America/New_York     2023-03-30 15:00:00-04:00
America/Vancouver    2023-03-30 12:00:00-07:00
US/Hawaii            2023-03-30 09:00:00-10:00
```

## Agenda

### Old Business
 
- [x] Plausible [name=Melissa] No updates (my fault!)

### New Business

- [x] RSE Reports
- [x] semgrep https://semgrep.dev They have been emailing me if they can sponsor (give us a free account?). Does this look interesting enough to anyone to be worth responding to?
- [x] [name=Melissa] New contributor meeting next week (Tuesday, 5pm UTC). No agenda, maintainers welcome!
- [x] GSoC - how/where can candidates ask questions?
    

### Issues and PRs

- [x] [name=@rcomer] Offset option in MultipleLocator: do we want this and if so is *offset* the best name for the parameter? [#25542](https://github.com/matplotlib/matplotlib/pull/25542)
- [x] [name=@chahak13] [#4672](https://github.com/matplotlib/matplotlib/issues/4672) Retrieve marker style info from scatter? If there isn't much interest, then can close this.
- [x] [name=@chahak13] [#6453](https://github.com/matplotlib/matplotlib/issues/6453) Small (_very_) size in scatter still has some sort of an overflow (at about e^-28 from a preliminary check). 

## Notes

### RSE reports
- @tacaswell More work on test image refactor. Astropy pytest-mpl workflow. Hashes of images, and if hash fails, get image and do image comparison. But requires freetype to be pinned
    - writing docs first to understand issues that need to be solved
- @ksunden
    - typing PR merged.
        - CI now run so should catch PRs that don't have stubs
        - some things skipped in CI. eg axes artists methods!  Devs should check  that signature changes are added to the stub including expanded type. 
        - IDEs can do type checking using the stubs.  Devs may want to use these.
        -  some docstrings improved (separate PRs generally)
        -  some return type inconsistencies that are to be done in follow-ups
        -  mypy doesn't check implementation to see if consistent with stubs
        -  questions about interfacing w/ external libraries: yes external libraries need to be consistent with our stubs, but internally we are not.
            -  internally examples should work with the stubs.
        -  stub files were used as first step...
        -  package installed, stub files installed as well
        -  try and test a few libraries?
            -  announce change on announce page at Discourse
        -  numpy type hinting w/ shape information?
            -  scientific python discourse?
    - PDF Preview.app difference...
- @QuLogic 
    - working on mpl-sphinx-theme and other doc repos
    - meson build tool instead of distutils.  
        -    Working on porting to Matplotlib.  Meant to be used w/ compiled projects.
        - possibly different on windows
- @melissawm 
    - GSoD submitted (response tommorow). Hire by mid May if selected
    - New contrib meet next week on Tuesday. Encourage new folks to come!
    - GSoC questions?  Who to talk to?  Pointing to project page.  Gitter channel exists, 
    - first issues
        - Need follow-up on a couple of these...

### Semgrep
- extra linting service
-  https://semgrep.dev  Follow up w/ @tacaswell if you think this is useful...

### Offset option in MultipleLocator [#25542](https://github.com/matplotlib/matplotlib/pull/25542)

 - do we want this and if so is *offset* the best name for the parameter?
     - maybe *shift*, *tick_offset*?  Moving ticks...
     - *offset* is fine.
 - seems reasonable
 - example of PR that will fail CI because of type stubs!
 
 ### [#4672](https://github.com/matplotlib/matplotlib/issues/4672) Retrieve marker style info from scatter? 
 - If there isn't much interest, then can close this.
 - Yes close
 
### [#6453](https://github.com/matplotlib/matplotlib/issues/6453) Overflow scatter
- Small (_very_) size in scatter still has some sort of an overflow (at about e^-28 from a preliminary check) that makes a large scatter?
- close as can't fix...  stroking issue and depends heavily on the backend...
- link to other issue with donuts...


---------------------
# 23 Mar 2023

```
2023-03-23 20:00:00+00:00
Europe/Berlin        2023-03-23 21:00:00+01:00
UTC                  2023-03-23 20:00:00+00:00
America/New_York     2023-03-23 16:00:00-04:00
America/Vancouver    2023-03-23 13:00:00-07:00
US/Hawaii            2023-03-23 10:00:00-10:00

2023-03-30 19:00:00+00:00
Europe/Berlin        2023-03-30 21:00:00+02:00
UTC                  2023-03-30 19:00:00+00:00
America/New_York     2023-03-30 15:00:00-04:00
America/Vancouver    2023-03-30 12:00:00-07:00
US/Hawaii            2023-03-30 09:00:00-10:00
```

## Agenda

### Old Business


### New business
 - [x] RSE reports
 - [x] Do we want to participate in Grace Hopper Conference sprint again?
 - [x] [name=Melissa] Plausible?
     - https://plausible.io/
     - Requires an update to the pages layout template ([Example from SciPy](https://github.com/scipy/scipy/blob/main/doc/source/_templates/layout.html), [where this could go for Matplotlib](https://github.com/matplotlib/matplotlib/tree/main/doc/_templates))
 - [x] [name=Melissa] Submitting the proposal for GSoD (deadline tomorrow)
     - https://hackmd.io/@matplotlib/gsod2023
     - Two technical writers interested already :tada:
     - Need a contact email for folks interested
 - [x] tag/index mechanics
     - related to above, but somewhat orthogonal as well, as the GSoD probably won't do the technical part

## Notes

### RSE reports....

- @tacaswell: Busy with BNL work
- @ksunden: issues/pr reviews.  Older units issues.  Typing PR, CI works for stub test
- @QuLogic: documentation.  theme; third-party-page needs to be updated.  Need fixes 3.7.1
- @melissawm: GSoD possible technical writers, 3 or 4 candidates.  Need to submit project proposal.

### GSoD
- put on wiki
- 3-4 possible candidates
- need an email for point-of-contact: organizational contact
    - personal email address OK.  
    - CV, statment of interest
        - did on public mailing list versus private
        - can wait until if we know we are selected.
- clairfy that guidelines of how to tag future examples + how to decide we need a new tag is part of the diveralble.
- change budget to be a single technical writere

### tags

- @melissawm has a worked prototype of adding a tag directive to sphinx (https://github.com/melissawm/sphinx-tags)
    - may move project under sphinx-gallery 

### GHC

- lots of work 
- maybe test coverage issues is good sprint work...
    - figure out missing code paths w/o image tests
    - missing tests for different data types...
        - exercise different data types (dates, categorical, pandas), perhaps just smoketests, or when image testing infrastructure in place....
- As "feature project"
    - numpy did this ~70 people; ~40 had a pull request...
- September 2023

> Thank you for participating in the Grace Hopper Celebration’s Open Source Day 2022. Because of that submission and your overall contributions to the open source community, we would like to invite you to, again, partner with AnitaB.org for GHC’s Open Source Day 2023!
>
>Open Source Day is always an exciting opportunity for attendees to learn and become open source contributors. Trained mentors provide guidance to make contributions to listed projects. Projects that participate in the event not only gain visibility and same-day contributions, but also benefit by widening their pool of future contributors. In the past, we have seen how positively impactful OSD can be for both the attendees as well as the projects involved.
>
>Given your outstanding involvement in open source, we would be really excited for you to join us again this year.
>
>Same as last year, OSD projects must have at least one woman or non-binary core maintainer and provide mentors and triaged, technical-focused, good first issues for the event. Maintainer/mentor teams will introduce the project, answer questions, and support attendees in making contributions. OSD projects will gain visibility and same-day contributions, as well as help grow the pool of future contributors. 
>
>
>
>Project maintainers require the following commitments: 
>
>·         Provide the minimum number of triaged issues (5+ for small projects, 30-100 for large projects) 
>
>·         Provide a short project overview 
>
>·         Attend full GHC 23 OSD event during the conference 
>
>·         Onboard three or more OSD-appointed mentors who will become contributors to your project, as well as guide participants on pull requests and troubleshooting and answer questions 
>
>·         Engage with and answer attendee questions on Slack and Zoom 
>
>·         Review and merge pull requests during OSD 
>
>If you are interested in participating this year, please submit your project via the GHC CFP. The GHC CFP process ends on April 26th, 2023. 
>
>If you are aware of or have any open source projects with female maintainers in your network whom you think are a great fit for this opportunity, please forward this email to them. We appreciate you helping us in this effort!
>
>We’re excited to work with you in 2023!

### Plausible

- https://plausible.io Google analytics replacement...
- more privacy respecting
- can run both at same time....
- should get snapshot of google analytics, maybe not lose that...
- google analytics wants us to change tags?
- scientific python has a server that runs plausible...
- we also get cloudflare analytics
- @melissawm to put in PR with `conf.py` change (if possible) or template change. 

-------------------
# 16 Mar 2023

Note time this week and next week if in North America:
```
Europe/Berlin        2023-03-16 21:00 (+01:00 CET)
UTC                  2023-03-16 20:00 (+00:00 UTC)
America/New_York     2023-03-16 16:00 (-04:00 EDT)
America/Vancouver    2023-03-16 13:00 (-07:00 PDT)
US/Hawaii            2023-03-16 10:00 (-10:00 HST)

Europe/Berlin        2023-03-23 21:00 (+01:00 CET)
UTC                  2023-03-23 20:00 (+00:00 UTC)
America/New_York     2023-03-23 16:00 (-04:00 EDT)
America/Vancouver    2023-03-23 13:00 (-07:00 PDT)
US/Hawaii            2023-03-23 10:00 (-10:00 HST)
```

## Agenda

### Old Business

### New Business
- [x] RSE reports


### Issues and PRs
- [ ] [name=@greglucas] Whether to add images that are knowingly bad for tests if they are a partial improvement? [#23199](https://github.com/matplotlib/matplotlib/pull/23199)
- [ ] [name=@greglucas] pcolor[mesh] proposal to return 2D array for data but 1D for get_facecolor? Issue: [#25162](https://github.com/matplotlib/matplotlib/issues/25162) PR: [#25027](https://github.com/matplotlib/matplotlib/pull/25027)
- [ ] MplGui 
- [x] mplcairo 
- [ ] https://github.com/matplotlib/matplotlib/pull/25210
- [x] [name=@chahak13] Old Issue: [PyAV movie writer](https://github.com/matplotlib/matplotlib/issues/4416)

## Notes

### RSE reports
- @tacaswell bug squashing (mem leak in font fallback); image regeneration prototype - test suite at external tree; will need tooling.  Nice way of changing and adding a new image test
    - discussed the workflow a bit this will entail
    - checking when freetype changes? 
    - pytest-mpl has a website viewer of failing images
- @ksunden mypy over examples.  
    - Some errors that need fixing in examples themselves.  mypy doesn't like re-using variable names for different things
    - PR review
    - planning for medium term projects
- @QuLogic
    - PR review
    - stale issues review
    - draft PR backlog (webagg testing; browser or framework issues)

### [PyAV movie writer](https://github.com/matplotlib/matplotlib/issues/4416)
- python interface to ffmpeg
- use only if you need to...
- probably a historical artifact when ffmpeg not as cohesive
- ship static wheels with ffmpeg
- maybe has threading?
    - maybe a really simple multiprocessing example would be useful
    - add comment with ffmpeg invocation...

### mplcairo

- C++ probably OK.
- Do we have maintenance expertise to keep going? 
    - a lot of the important code is probably C++
    - plumbing is in python
- getting within realm of possibility
- cairo and agg at similar levels of maintenance
    - not sure about current agg 
    - cairo has few developers.
    - GL backends maybe more popular...
        - less concern about anti-aliasing these days due to higher res displays.

### mplgui
- pyplot:
    - keeps global state
    - manages GUI event loop
        - global registry of open figures
- mplgui does second without implicit global state
    - can have `Figure` objects created separately, and push to GUI when we want.
    - also has a Figure registry
    - 
- how to pull into main library?
- fig.show()  ?  Can't show multiple figures...
- mg.show(figs) would open many figures....
- rewrite the pyplot interface on top of this?






--------------------

# 9 March 2023

_attending_: 

## Agenda

### Old business

### New business
- [x] Next week Americas DST transition:
    ```
    Europe/Berlin        2023-03-16 21:00 (+01:00 CET)
    UTC                  2023-03-16 20:00 (+00:00 UTC)
    America/New_York     2023-03-16 16:00 (-04:00 EDT)
    America/Vancouver    2023-03-16 13:00 (-07:00 PDT)
    US/Hawaii            2023-03-16 10:00 (-10:00 HST)
    ```
- [x] RSE reports
- [x] 3.7.1 release?
- [x] Stale label? 

### Issues and PRs

- [x] [name=@chahak13] Comments on https://github.com/matplotlib/matplotlib/pull/25259 (size for markers in scatter)
- [x] [name=@ksunden][initial typing implementation](https://github.com/matplotlib/matplotlib/pull/24976/)
- [x] [name=@jklymak][Tutorial and User doc overhaul](https://github.com/matplotlib/matplotlib/pull/25395)
- [ ] [name=@greglucas] Whether to add images that are knowingly bad for tests if they are a partial improvement? [#23199](https://github.com/matplotlib/matplotlib/pull/23199)
- [ ] [name=@greglucas] pcolor[mesh] proposal to return 2D array for data but 1D for get_facecolor? Issue: [#25162](https://github.com/matplotlib/matplotlib/issues/25162) PR: [#25027](https://github.com/matplotlib/matplotlib/pull/25027)
- [ ] MplGui (maybe next week)
- [ ] mplcairo (maybe next week)
- [ ] https://github.com/matplotlib/matplotlib/pull/25210


## Notes

### RSE reports

- @ksunden: fresh issues (memory "leak"). Metatdata issue on figsave. Typing PR (sphinx warnings...)
- @QuLogic 3.7.1 release!  Issue triage older ones closed.
- @melissawm: new contributor off time meeting.  Two new people.  @saranti @devrd attended.  Very engaged... https://github.com/matplotlib/matplotlib/pull/25210
- @tcaswell: issue triage.  Testing images into separate place to move freetype.

### 3.7.1
- crtical bugs out.  No new issues so far.  

### Stale
- maybe caught up to milestone changes...
- can we ignore milestones in stale bot?


###  [markersize on scatter](https://github.com/matplotlib/matplotlib/pull/25259)
- 'markersize' instead of 's'.
- kwarg for scaling
- get_sizes?  should return original or transformed size?

### [initial typing implementation](https://github.com/matplotlib/matplotlib/pull/24976/)
- _many_ errors w/ mypy
    - most explicable
    - @ksunden has tool for doing this...
    - sphinx warning...
- mark as ready for review
    - independent of run-time
    - editor integrations may be better
- does testing tell us if stubs get out of sync?
- compatibility with Microsoft stubs?
    - choose one or other, which one?
    - PR to Microsoft?
    - or Microsoft will perhaps remove when we release? (panadas was removed)
- things that should get eyes on:
    - anything that touches .py files (only thing will affect run time)
        - `__init__.py` picked up a `__all__`
        - pyplot has inline type hints (because it is partially auto-generated)
        - change to boilerplate.py
        - using black for autogenerated parts of the code
            - adds black as a test + dev dependency
        - added a typing module (provisional)
            - importable top-level module to hold type aliases (e.g. color, linestye)
            - makes users like a bit less annoying if they want to type hint their code using Matplotlib
        - some types in test
            - there to make it possible to run mypy on 
    - linked to Dask's guide lines
        - we may want to adopt these, but not fully done yet
    - run on examples?


### User guide re-org
 - user guide is bare
     - mostly just explaination
 - one the other hand tutorials section had lots of user guide type things
     - colors
     - imshow extents
     - text, annotation, ...
 - the user guide is in rst, tutorials are in SG
 - thus the material is organized by tools rather than by content
 - worked with SG to make it possible to mix rst and .py in the same tree 
     - got this merged upstream
 - SG used to use a custom README.txt to build the index, now can override this behavior by by having an index.rst to give you full control
 - did re-organization
     - including fixing all of the internal cross references
 - Caswell executive decision to deletage merge authority on this to Jody to self-merge when he thinks it is ready
     - at least 1 week more discussion