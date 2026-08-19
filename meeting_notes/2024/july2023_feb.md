# Matplotlib Weekly Meeting 

[![hackmd-github-sync-badge](https://hackmd.io/jd_7FjxNQ4y7XgNknvmvGQ/badge)](https://hackmd.io/jd_7FjxNQ4y7XgNknvmvGQ)

**A regular sync meeting for the project's maintainers, which is open to the community.** Everyone is welcome to attend and contribute to conversations.

## 27 July 2023 -- February 15 2024


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
# 15 Feb 2024

_attending_: @tacaswell, @ksunden, @story645, @timhoffm, @QuLogic 

## Agenda

### Old business

- [x] RSE reports
- [x] 3.9 progress
- [x] scipy tutorial planning

### new business

 - [x] 3.7 and 3.8 micro release

### PRs
 - [ ] [name=hannah] [violinplot color API](https://github.com/matplotlib/matplotlib/pull/27304)

## Notes
- start new notes for next week
### RSE reports
 - Kyle
     - 3.8.3 tagged out out the door
     - 3.7.5 release in the works
     - dataprototype work
     
 - Tom:
     - some triage / review work
     - data prototype meetings
 - Elliott
     - video work in the docs
         - now 2 projects deeps
     - will do 3.7.5 today
     
 
### scipy tutorials
 - asked scipy chair for what they want -> want interactive
     - https://github.com/matplotlib/interactive_tutorial exists and likly still works
 - keep stucture from last year, but change focus
     - move from just building up grid, focus on concepts
 - @story645 has some ideas / material on interactive as well

### 3.9 status

- still looking good for RC in March

### violinplot colors

- (color, facecolor, edgecolor) like bar vs. parameter dict violinprops like boxplot
- consensus: facecolor + edgecolor, and add alpha, vectorize facecolor

# 08 Feb 2024

_attending_: @ksunden, @tacaswell, @efiring, @timhoffm, @IGuKs80UTJCig4yt6Zos7w (greglucas), @story645, @shriyakalakata, @QuLogic 


## Agenda

### Old business

- [x] RSE reports
- [x] 3.9 progress reports

### New business
- [x] [name=ksunden] Locking down/deleting the Github wiki
- [x] [name=greglucas] Scipy plans https://www.scipy2024.scipy.org/

### Issues and PRs
- [x] [name=QuLogic] [bump minimum NumPy requirement](https://github.com/matplotlib/matplotlib/pull/26800)
- [ ] [name=hannah] [using labels for "don't merge"](https://github.com/matplotlib/matplotlib/pull/27668)
- [ ] [name=hannah] [usage content guide](https://github.com/matplotlib/matplotlib/pull/26389)
    - [rendered page](https://output.circle-artifacts.com/output/job/4770a68d-dcb5-446e-8ca5-b58000f4e974/artifacts/0/doc/build/html/devel/document_content.html)


## notes
### RSE updates
 - Kyle
     - data prototype work: integrating ideas with drawing stack, playing with very simple layers
     - worked on OSX hang issues (with Tom and Elliot)
     - general maintence
     - GSOC
 - Elliott
     - 3.9 progress
     - getting CI PRs up and working
     - closed the last deprecation removal PR
     - change laptop back to linux
 - Tom
    - osx bug, other review
    - paper work
    - now have a windows VM that can test on

### 3.9 progress?
- making progress
- still looking good to hit March
- please review pybind11 PRs

### wiki
- was world writable
    - locked down now
- do we want to keep at all?
- can we archive it?
    - either add it to an exsiting one (project managment)
    - add git repo that backs it to org and then mark as public archive
- seem to only use it for GSOC ideas / propsoals
- have a duplicate copy of MEPs
- propsoal (accepted with no prost)
    - upload and public archive repo
    - removing from GH
    - never talk about again
    - will have to change this years GSOC links

### scipy plans

- do we need to submit stuff
    - sprints: probaly not
    - tutorial: need to get something in on time (Feb 27)
        - re-run the layout one from last year (if Kyle leads)
    - talk:
        - data work (still thinking)
- going
    - Greg
    - Kyle
    - Hannah (maybe)
    - Elliot (if we have funding)

### numpy version

- in March we should be Python 3.9 / numpy 1.23
    - jump 2 numpy versions and get back on track
- for numpy 2.0 things built with 2.0 will work with numpy 1.x but things built with 1.x will not work with 2.0
    - should be able to just build everything with 2.0 and not worry about oldest supported

### no merge on labels

- no runs with on premissions
- but needs to pass if it should not block merging

### content guide

Caswell would like to push content guide until Jody is here

# 01 Feb 2024

_attending_:
@tacaswell @ksunden @story645 @QuLogic 


## Agenda

### Old business

- [x] final decision on GSOC
- [x] RSE reports
- [x] 3.9 progress reports

### New business
- [x] [name=hannah] [using labels for "don't merge"](https://github.com/matplotlib/matplotlib/pull/27668)

### Issues and PRs
- [ ] [name=QuLogic] [bump minimum NumPy requirement](https://github.com/matplotlib/matplotlib/pull/26800) (to next week)
- [x] [name=hannah] [user/project to project](https://github.com/matplotlib/matplotlib/pull/27560) 
- [ ] [name=hannah] [usage content guide](https://github.com/matplotlib/matplotlib/pull/26389) (to next week)


## notes

### memory leak test

- takes around 200 iterations for memory usage to "burn in"
- this takes at least 50 seconds
- our tests with a burn in of 2 and test of 5
- we will rip the test out and open an issue for new weekly test to check memory

### azure failures

- add manual timeout to popen test
- add retry to these tests?
- maybe related to xvfb issue like hang during collection?

### GSOC
- ask NF for 1 slot
- visual search project
    - concern that this is would be an acceptable GSOC project

### RSE reports
 - Tom: reviews, little bit of testing improvements, meeting with Kyle tomorrow to talk about NASA
 - Kyle:
     - data prototype project
     - trying to actulaly use prototype
 - Elliott:
     - CI work (m1s are now available on github)
     - documentation work
         - change animation format from list of frames to actual video
         - saves space!
         - work upstream with sphinx gallery
         - some examples may see 20x reductions
         - costs us frame-by-frame playback
 
### 3.9 progress
 
 - still making progress
 - need to discuss
     - numpy bump
     - linear rescaling of marker size

### don't merge via labels

make it possible to label as "this needs discussion" differently from "I have specific code changes"




# 25 Jan 2024

_attending_: @rcomer, @ksunden, @qulogic, @tacaswell, @story645 

### Old business
- [x] RSE reports
- [x] 3.9 progress report

### New business
- [x] GSOC: numfocus deadline is Feb 5th
    - [ ] https://github.com/numfocus/gsoc/tree/master/2024
    - [ ] https://summerofcode.withgoogle.com/programs/2024
### Issues and PRs
- [x] [Make singular colorbars consistent with single-value mappables.](https://github.com/matplotlib/matplotlib/pull/26307)
- [x] [Add `U`, `V` and `C` setter to `Quiver`](https://github.com/matplotlib/matplotlib/pull/26410) - API question on setter for UVC/data/offsets
- [x] [Add widths, heights and angles setter to EllipseCollection](https://github.com/matplotlib/matplotlib/pull/26375) - getters?
- [ ] [Added optional props argument to Lasso Widget `__init__` to customize Lasso line](https://github.com/matplotlib/matplotlib/pull/26594)
- [ ] [Fix 

legend entries](https://github.com/matplotlib/matplotlib/pull/27568)
- [ ] [Fix behaviour of Figure.clear() for SubplotParams](https://github.com/matplotlib/matplotlib/pull/27183)
- [ ] [Allow linear scaling for marker sizes in scatter](https://github.com/matplotlib/matplotlib/pull/25259)

## notes

### RSE updates
- Kyle: 
    - work on data prototype work
    - re-thinking how to manage and optimize the graph of computations
    - small PRs / review
- Elliott
    - smallish review things
    - have windows on arm working
        - mostly just worked, pushed freetype back to our old version.
        - only see timeouts on interacitve tests (maybe resources due to paralle)
        - did not need any extra tolerances
    - have a PR for linting + validtion of all of our yaml
        - prevents a class of bugs, some issues with source of schemas
        - should catch errors in yaml that are currently only caought by running on main after merge
- Tom
    - data prototype work
    - EffVer PR
    - some review

### mpl3.9 
- making steady progress
- bunch of PRs on todays agenda
- jupyterrfb?
    - maybe not for 3.9
    - small quality of life stuff needs to be merged upstream (cursors + rubber band)
    - still have to work out restart / stop / snapshot
        - likely due to us wrapping it in additional widgets (box + toolbar) so snapshotting looks wrong

### GSOC

- do we have good projects?
    - hatch API?
        - not great because API design is hard
    - heigharchical ticks
        - same problem
    - reach out ot multi-variate colormap contributor
- who has effort?
    - kyle

# 18 Jan 2024
_attending_: @QuLogic, @ksunden, @tacaswell, @ianthomas23, @greglucas, @anntzer

## Agenda

### Old business
- [x] RSE reports
- [x] 3.9 progress report

### new business

- [x] backend + ipython https://github.com/matplotlib/matplotlib/issues/27663
- [x] adopt EffVer https://jacobtomlinson.dev/effver/
- [x] [name=hannah] [violinplot color parameters](https://github.com/matplotlib/matplotlib/pull/27304)
- [x] [name=hannah] [stream plot n_arrow](https://github.com/matplotlib/matplotlib/pull/27617)
- [ ] [name=greglucas] macos warning out of our control? ([27389](https://github.com/matplotlib/matplotlib/issues/27389))
- [ ]  start next weeks note -> date + field at end of meeting

## Notes

### RSE updates
- Kyle: 
    - preperations for pytest8+ numpy2
    - design work on data prototype 
- tom:
    - general issue review + prototype supportwork
- elliott:
    - pybind11 work
    - working on window-on-arm test machine setup again

### 3.9 progress

- still have a couple of deprecation removals outstanding
    - finish PRs from new contributors
- some PRs that are adding new deprecations we might want toget in
    - put on agenda for next week

### EffVer

Better description of what we currently do

"stamping current policy with better name"

### parameters in violiplot

should we do it like `ax.bar` or `ax.boxplot`

### ipython + Matplotlib integration 

- `%matplotlib` can be used to select backends
- list of supported backends currently hard-coded into ipython
    - includes built in Matplotlib backends
    - and 2 jupyter specfic backends
- includes a mapping from backend <-> gui framework
- odd that the hard-coded backend lives in IPython
- how do we support external backends
- use entry points for backends to declare them selves
     - could put this in IPython and problem most locally
- better solution is registry to live in Matplotlib
    - supports entry-point registraion
    - supports hard-coded ones we ship
    - support `module://` as well

comments
 - IPython `%matplotlib ...` could support `'module://'` as input
 - concern about `%matplotlib` doing surprising imports
 - concern about alias
     - no alias scheme
 - order of lookup
     - builtin names (maybe include all current names (inline, widgets, notebook))
     - entrty points
         - if collisions fail hard and ask to uninstall one
 - should make IPython respect the `required_interactive_backend`

do we want to try and seperate GUI selection + renderer selection
 - yes, but does not currently factor nicely
 - some agg specific assumptions in the source


### need help with mplcairo

- sort out why not compatible with mpl3.9
- can we move mplcairo into mpl-main to replace exsiting cairo
    - depends on how we want to load cairo
    - we may need to build cairo for wheel
        - mplcairo currently depends on pycairo to steal their
          dll/so
    - some extra text handling
        - one is cairo's font handling
        - one is based on raqm
- maybe try to do this with a SDG

# 11 Jan 2024

__attending__:
## Agenda

### Old Business

### New Busines
 - [] RSE reports
 - [] 3.9 target date

### Issues and PRs
- [ ] [name=QuLogic] https://github.com/matplotlib/matplotlib/pull/27310
- [ ] [name=greglucas] [QuadMesh nan vertices](https://github.com/matplotlib/mplcairo/pull/54) Different backends treat the quads differently. Would we want to assert anything in how this is handled?

## notes

### RSE updates
- Kyle: catching up after 2 weeks off
- Elliott: catchup, looking at CI
    - finishing up autopublishing
    - trying to get labelling working
- Tom: issue / PR review, busy with other work

### Issues 
 - https://github.com/matplotlib/matplotlib/pull/22699
    - merged
- https://github.com/matplotlib/matplotlib/pull/27310
    - meant to leave comment last week, now posted
- https://github.com/matplotlib/mplcairo/pull/54
    - we should let quadmesh and the functions that call them take `np.nan` in x/y
    - should poison entire quad that the nan is in
- https://github.com/matplotlib/matplotlib/pull/27563
    - merged 
- https://github.com/matplotlib/matplotlib/pull/27624
    - needs a bit more work
- https://github.com/matplotlib/matplotlib/pull/27618/
    - switch back to py39
    - remove broken to prove broken commit
- https://github.com/matplotlib/matplotlib/pull/27552
    - need to add note about how to run with `python -m pytest`
- https://github.com/matplotlib/matplotlib/pull/27230
    - @IGuKs80UTJCig4yt6Zos7w will look at
- discussion about managing font caches
    - ensure that cache is generated docs
    - add a CLI to font manager to help with cache genartion / clearing / locating
    - maybe add a mode to only use fonts we shpsic

# 4 Jan 2024
@tacaswell @story645 @QWhXj01mSwmTjk5kN1H_qQ (@efiring) @IGuKs80UTJCig4yt6Zos7w (@greglucas) @QuLogic 
## Agenda

### Old Business
- [x] Meeting time discussion 

### New Busines
 - [x] RSE reports
 - [x] 3.9 target date
 - [ ] 
### Issues and PRs

- [x] [name=QuLogic] https://github.com/matplotlib/matplotlib/pull/27310
- [x] [name=Hannah] [Content guidelines](https://github.com/matplotlib/matplotlib/pull/26389)
- [ ] [name=greglucas] [QuadMesh nan vertices](https://github.com/matplotlib/mplcairo/pull/54) Different backends treat the quads differently. Would we want to assert anything in how this is handled?

## notes

### meeting discussion

 - hour earlier slightly better in poll, but keep same time for now
 - split triage discussion from broader discussion
     - 1st & 3rd policy
     - 2nd & 4th triage
 - RSE reports have been very helpful

### RSE updates
 - Tom: issue review + PRs
 - Elliott: off last week
 - Kyle: off

### 3.9 release
 - @QuLogic release manager
 - target march
 - when is numpy 2.0 targeted to
     - https://github.com/numpy/numpy/issues/24300
     - do a 3.8.x along with numpy's 2.0 rc to drop the pin
     - this lets us de-couple mpl3.9 from numpy2.0
 - rcs in late Feburary
     - beat Fedora beta-freeze with our RC (by Feb 20)

### Docs

- link back to diataxes in each section
- break out user guide into start-> build -> create 

### SymLog
