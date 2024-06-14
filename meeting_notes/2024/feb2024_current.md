# Matplotlib Weekly Meeting 


**A regular sync meeting for the project's maintainers, which is open to the community.** Everyone is welcome to attend and contribute to conversations.

## February 22 2024 - 


###### tags: `2024 dev call`


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
# June 13
_attending_: 

## Agenda

### Old business
- [x] RSE
- [x] GSOC
- [x] SDG
- [ ][name=hannah][homepage translation](https://github.com/matplotlib/mpl-brochure-site/issues/93)
    - do we want to instead pilot the tooling on cheatsheets cause [demand](https://github.com/matplotlib/cheatsheets/pull/132)

### new business
 - [x] report from dev summit
 - [ ] plan for 3.9.1


## Notes

### dev summit

- about 40 people in Seattle
- lots of discussion about SPECs
    - https://scientific-python.org/specs/
    - endorsed the two we already do (timeline + uploading nightly wheels)
    - supply-chain related work relevant for us
    - other are not relevant
- talked with Thomas Fan about WASM builds
    - pyodide has updated build system so that projects can build
    - have it working again, but font loading is broken
        - our optimaztion settings make debugging hard (no symbols names)
    - cibuldwheel can build wasm "wheels" without patches (but does not work)
        - may need to be aware of filesystem sandbox

### RSE
 - SDG went
 - data prototype 

### GSOC
 - have a plan for how to organize PR in to work
 - ongoing discussions of code organizations

### 3.9.1 
 - a TK bug which has been fixed
 - sticky edges on bar bug (PR soon)
 - add back cm.get_cmap 
     - some users did not see warning
     - Tim has a PR to put it back
     - Greg and Tom say to put back temporarily
     - question about why users didn't see
         - Tom: is this due to the warning class we use that users never saw it
         - Greg: is this users jumping a bunch of versions
 - other color related questions (behavior of color maps with int intputs) https://github.com/matplotlib/matplotlib/issues/28198
 - should we also add `lut=` to the mapping registry version?

# ~~June 6~~ CANCELED 



# May 30 
_attending_: @efiring, @oceanwolf @QuLogic @tacaswell @story645 @IGuKs80UTJCig4yt6Zos7w (gregluca) @rcomer @ksunden 

## Agenda
### Old business
- [x] RSE
- [x] GSOC
- [x] SDG - due tomorrow 31st

### New Business
### Issues & PRs
- [ ] [name=hannah][homepage translation](https://github.com/matplotlib/mpl-brochure-site/issues/93)

## Notes
### RSE
- Elliott
    - SDG writing
    - reveiwing stalled new contributor PRs
    - finish some high-dpi fixes for cairo
- Kyle
    - thinking about grant stuff
    - some review
    - GSOC has started
- Tom
    - grant stuff
    - some issue review
    - work on grant reports

### GSOC
- breaking up current big PR into smaller chunks
- looking at git + rebasing tools to help with breaking up into parts

### SDG
 - has draft
 - adobe is adding support to add alttext to images
     - do what they do!
 - discussion of details of raqm / freetype interaction

### issues / PR
 - translating the brochure page
 - questions about how the tooling works
 - how do the translations get maintained going forward?
 - what is exit strategy?
 - is this actually of value to anyone?
 - @story645 will take point on sorting it out

### CF
- work still needs to be done for 3.9


# May 23
_attending_: @efiring, @ksunden @tacaswell @story645 @QuLogic 

## Agenda
### Old business
- [x] RSE updates
- [ ] SDG state
- [ ] ROSES state

### New business
- [ ] 3.9 release fallout?


## Notes
### RSE updates
 - Tom
     - avoid writing grants by responding to issues on GH
 - Kyle
     - also working on grant
     - issues on github

# May 16 
_attending_: @efiring, @QuLogic, @tacaswell, @ksunden, @story645 
## Agenda
### Old business
- [ ] RSE updates
- [x] GSOC update

### new business

- [x] 3.9 is out!
- [x] SDG followup


## Notes
### 3.9
 - we added an import that seems to break, but we think that is a local install issue.
- promote `:mpltype:` to be public (otherwise downstream packages that inherit our docstrings will break)
     - what else do we need to make public?
     - The set of thing that look like roles the show up in our source (generated via ``set($(ack ':[^:]*:`' -o -h --python).split())`` )
```
{'::`',
 ':align:`',
 ':alt:`',
 ':attr:`',
 ':caption:`',
 ':class:`',
 ':context:`',
 ':data:`',
 ':doc:`',
 ':download:`',
 ':envvar:`',
 ':file:`',
 ':format:`',
 ':func:`',
 ':height:`',
 ':include-source:`',
 ':math:`',
 ':mathmpl:`',
 ':meth:`',
 ':mod:`',
 ':mpltype:`',
 ':nofigs:`',
 ':program:`',
 ':rc:`',
 ':ref:`',
 ':scale:`',
 ':show-source-link:`',
 ':sup:`',
 ':target:`',
 ':width:`'}
```

We think only rc, or mpltype need to be moved up. (@qulogic will do).

## GSOC

- Had kickoff meeting before start of main coding period (starts week after next)
- need plan for how to get in
- maybe do not do auto inference at all
- how to handle complex data?
- sequencing
    - first PR: 1 norm, 1 colormap
    - follow on PR: additional colormaps
    - follow on PR: complex support
    - follow on PR: add more norms
    - follow on PR: how to combine VectorMappable and ScalarMappable?
- open questions
    - don't have "over" and "under" but still need "in bounds" vs "bad"
        - to handle out of bounds:
            - fixed color
            - pick "closest" point and use that
    - cartesian or polar coordinates in color space?
    - how to handle categorical
    - legend/colorbar


## SDG

- still being drafted
- focus on accessibility
    - embedding alt text into output meta-data (as discussed last week)
    - font overhaul work


## RSE update
 - Tom
     - grant work + avoiding grantwork by doing issue review
 - Kyle
     - some grant work, data prototype stuff
 - Elliott
     - Jury duty selectiono
     - 3.9 release 


# May 9
_attending_: @tacaswell, @greglucas, @QuLogic, @ksunden, @story645, @trygve

## Agenda
### Old Business
- [x] RSE
- [x] 3.9
- [ ] 3.10

### New Business
- [ ] [name=hannah][numfocus small dev grant](https://numfocus.typeform.com/to/mbtH7w) due May 31st

## Notes
### old business
 - Kyle
     - planning meeting for developer summit
     - meet with a NASA project on Monday
     - working on data prototype
     - helping with on 3.9 wrapup
 - Elliott
     - developer summit meeting
         - array protocol, supply chain validation work
     - 3.9 doc wrapup
     - mpl-sphinx-theme tagging
     - waiting for backports
     - maybe bug with old (>1yr) IPythons
     - tag today or tomorrow
 - Tom
     - mostly off

### small development grants
- Hannah will talk to Jni about feasibility of visual search
- hatches
- RFB work
- pull small/medium projects from CZI grant
    - saving alt text in image metadata
    - needs a plan for figuring out how screen readers read images
    - Elliot is drafting proposal


# May 2

_attending_: @tacaswell @story645 Ian Thomas @ksunden @QuLogic 

## Agenda
### Old Business
- [x] RSE
- [x] 3.9
- [ ] 3.10

### New Business

## Notes
### old business
#### RSE
 - Kyle
     - writing new NASA grant work
     - continuing interacitvity and contains in dataprototype
     - GSOC has been annouced, got 1 slot, need to reach out to start work
 - Elliott
     - reviewing Ian's PR
     - went through all the 3.9rc failures and opened issues or PRs for everything
     - working on getting api changes / whats new rolled up
     - do we want rc3?
         - IPython is happy without one
         - so no RC
     - planning meeting for scientific python developers summit tomorrwo
 - Tom
     - some issue/PR review
     - work on NASA grant.

### New business

#### anyone going to pycon
- Pavel (social media) and Chahak

#### IPython integration
 - almost done
 - last thing for 3.9 final

#### appveyor failures due to sphinx gallery
- due to upstream changes in sphinx/sphinx-gallery
- only see on appveyor because other CI systems do not install sphinx+sphinx-gallery
    - install from conda environment file
- PR existing to fix it (#28103)


# April 25

_attending_: @tacaswell @QWhXj01mSwmTjk5kN1H_qQ (Eric) @QuLogic @ksunden @story645 

## Agenda 
### Old Business
- [x] RSE updates
- [x] GSOC updates

### New Business
- [x] NASA propsoal
- [x] 3.9 status
- [ ] 3.10 piorities

## Notes
### RSE updates
- Kyle:
    - data prototype work, pushing on interactivity and contains
    - issue / PR work
    - some 3.9 issues down stream w/ Elliott
- Elliott:
    - catch up from vacation
    - no 3.9rc reports
        - do we know if it actually being tested?
    - ran rebuild in fedora
        - https://copr.fedorainfracloud.org/coprs/qulogic/mpl39/builds/ vs https://copr.fedorainfracloud.org/coprs/qulogic/mpl39.checker/builds/
        - only 10/130 new failures due to our RC
            - use of mpl.cm.get_cmap which was removed
            - use of plt.cm.get_cmap
            - new warning in python-mne (on legend with no entry)
            - mplcursors text changed, fixed upstream need a release
            - animatplot-ng sees effects of 3D limits change
            - may have broken pandas (preexisting unrelated failure on fedora, so did not test)
    - seaborn looks good with 3.9!
    - https://www.pepy.tech/projects/matplotlib?versions=3.8.4&versions=3.8.3&versions=3.8.2&versions=3.9.0rc2
- Tom
    - more progress on NASA grant

### GSOC

- have submited our ranking
- not heard anything back

### NASA
 - headline projects
     - cartopy to new data/artist model
         - work into how to integrate into existing structued data in that space
     - go all-in on pyodide (https://github.com/matplotlib/matplotlib/issues/27870)
         - https://github.com/pyodide/matplotlib-pyodide both agg and htmlCanvas backends exist
     - partner with a NASA mission to wrap interesting data
 - lots of maintence and support


### 3.10 priorities
 - colormapping work
 - 

     
# April 18

_attending_: @tacaswell @ksunden @QWhXj01mSwmTjk5kN1H_qQ (Efiring) @story645 

## Agenda

### Old business
- [ ] RSE

### New Business
- [x] [name=hannah] noting meeting attendance
- [ ] [name=hannah] [dedup hatch validation](https://github.com/matplotlib/matplotlib/pull/28076)

## Notes
### RSE
 - Tom:
     - grant work
     - issues review
 - Kyle
     - little bit of issues review
     - data prototype work

### attendance
Please remember to take attendance at meetings

### hatch validation
* https://github.com/matplotlib/matplotlib/pull/28076
 
 
### Data prototype

Just in time data + encoding and transform graph = visualizing large high dimensional multivariate datasets more consistently in less lines of code. 

just in time computation:
1. computational graph w/ delayed evaluation
2. querying and subsampling such that:
     1. computational datasets can be shown at various resolutions
     1. only subset needs to be loaded in memory/visualized

dynamic encoding:
1. more consistent way to give mappings in multiple artists ([Hullman & Qu](https://ieeexplore.ieee.org/abstract/document/8017651/))
2. treats the data fields more consistently with respect to encodings 

property syncing on artist:
1. artists can be reused
2. don't need to be manually updated individually 

why graph:
1. doing transformations, need to maintain/keep track of order for consistency
2. its inspectable in a way current isn't
3. can be broken down into smaller chunks, can add custom mapping
4. moves current implementation graph to data structure

tradeoff:
1. lots of encodings across different axes and artists - easier to reuse/share be
    * it's currently named different things in different artists
    * attaching the encoding function/mapping/$\nu$ to the artist
    * ex: color coding by category in line and scatter plot
    
Draw time querying + reducing the amount of info artists need to know about themselves facilitates real time data and reusing parts of the visualization. 

# April 11

_attending_: @tacaswell @jklymak @pXw4hSgTQF2--OciPYwa1w @QWhXj01mSwmTjk5kN1H_qQ (Anntzer), @IGuKs80UTJCig4yt6Zos7w (Efiring) @ksunden @QWhXj01mSwmTjk5kN1H_qQ 

## Agenda

### Old business
- [x] RSE updates
- [x] GSOC/GSOD

### New business
- [x] [name=tacaswell] default to RGBA stage interpolation https://github.com/matplotlib/matplotlib/issues/21167
- [ ] [name=saranti] [orientation parameter to violinplot](https://github.com/matplotlib/matplotlib/pull/27998)

## Notes
### grant recap
### RSE updates
 - Kyle
     - data prototype
         - clipping and images in new system
     - some 3.9
     - GSOC
 - Tom
     - grant stuff
     - review

### GSOC updates
 - reviews mostly done

### RGBA interpolation
- should remove clipping anyway
- should look Antony's suggestion of how to filter AA's data to clean up "fuzz" on constant data
- look into making the deault interplotaion stage depend on ratio between data pixels and screen pixels
- conclusion:
    - we will look at how to add an 'antialiased' interpolation stage
        - use same criteria as current antilaised flip
        - data space when upsampling
        - RGBA spacing when down sampling

# April 04
_attending_: @efiring, @ksunden, @tacaswell, @rcomer, @story645, @timhoffm, @QuLogic  

## Agenda
### Old business
- [x] RSE updates
- [x] GSOC / GSOD updates

### New business

- [x] 3.8.4 out!
- [x] 3.9.0 status?
- [x] NASA ROSES 2024 F7
- [ ] Colorbar snapping https://github.com/matplotlib/matplotlib/pull/26307

## Notes

### old
#### RSE updates

Kyle:
 - got 3.8.4 out
 - general review
 - data-prototype work
 - thinking about next NASA grant

Tom:
 - NASA grant
 - issue / bug review

Elliott:
 - prep for 3.9

#### GSOC / GSOD
 - missed GSOD deadline
 - GSOC
     - have 6 propsoals, look good
     - (not including detailed notes as these are public and do not want to break GSOC rules)
 - need more mentors
     
### new
#### 3.9.0rc status
 - was waiting on 3.8.x mergeup
 - should branch and tag today

#### NASA funding 
- trying to make formal friends
- looking for citations from all SMD
- looking for reviewers
- cartopy may also may be putting one in

#### singular colorbars
 - https://github.com/matplotlib/matplotlib/pull/26307#issuecomment-2038181561

     
# March 28
_attending_: @efiring, @ksunden, @story645, @trygvard, @QuLogic,

## Agenda

### old business

- [X] RSE updates
- [x] [name=hannah] GSOC apps due April 2nd, 1800UTC (next Tuesday)

### new business

- [ ] [name=ksunden] Last item I'd like for 3.8.4 [#27955](https://github.com/matplotlib/matplotlib/pull/27955)

## Notes

### RSE
- qulogic: working on Mac bugs; other PR reviews to finish off 3.9
- ksunden: also working on Mac bugs; tracking numpy 2; pybind11 fix for np2 released; all of blockers are gone for np2 micro-release; Ian released contourpy for np2; work on data prototype (lines, clipping, images); thinking about next NASA grant.

### New business




# March 21st

_attending_: @efiring, @ksunden, @QuLogic, @trygvard, @story645  

## Agenda

### old business

- [ ] RSE updates

### new business

- [ ] [name=timhoffm] https://github.com/matplotlib/matplotlib/pull/26307

## Notes

### RSE 
- qulogic: m1, pybind11, wrapping up 3.9, bouncing tasks to 3.10
- ksunden: 
    - pybind11, numpy 2.0, m1 (ksunden has it locally), 
    - dataprototype - dijkstra's algorithm & visualizing graph
- 3.9 : beta/rc soft deadline is next week 
- 3.8.4: numpy2.0 compliance, is on numpy timeline

### singular colorbars
- milestoned to 3.9, needs a decision from @tacaswell and @timhoffm 

### multivariate colorbars
- gsoc proposal draft, scope of project & components 

### 3.9 followups
- follow up about sphinx-tags multiline
- 

# March 14th

_attending_: @tacaswell, @efiring, @timhoffm, @QuLogic, @ksunden, @rcomer, @story645, @artemkislovskiy

## Agenda

### old business

- [x] RSE updates
- [ ] [name=hannah] steering council deadlines/turnaround
    - discuss at end of call
    
### new business
- [x] numpy 2.0 status
- [x] 3.8.4 release?
- [x] 3.9 status
- [x] [name=QuLogic] [Cursor coordinates on twinned Axes](https://github.com/matplotlib/matplotlib/pull/25556)
- [x] [name=QuLogic] [Avoiding levels in AutoDateLocator](https://github.com/matplotlib/matplotlib/issues/26363)
- [x] [name=QuLogic] [Decide what to do with `cycler` duplicates](https://github.com/matplotlib/matplotlib/issues/26868)
- [x] [name=QuLogic] [Return filename from save_figure](https://github.com/matplotlib/matplotlib/pull/27766)
- [x] [name=Hannah] [branch protection w/ labels](https://github.com/matplotlib/matplotlib/pull/27668)
- [x] [name=Tim] [Revert renaming labels to tick_labels in boxplot_stats()](https://github.com/matplotlib/matplotlib/pull/27916)

## Notes

### Intros

### RSE updates

- Elliott
  - mostly getting ready for 3.9
  - macos M1 CI jobs (lots of low tolerance image failures)
  - big triage push of 3.9 issues/PRs
      - took out 1/3, lots of docs left so not blockers for branching
  - pushed updates / rebases to existing PRs
- Kyle
    - 3.9 wrap up work
    - continuing work on data prototype work
    - numpy 2.0 fallout
        - mostly via pybind11, but may need to add a #define
        - some waiting on dependencies
        - in trianuglation and non-default contouring modes
- Tom
    - 3.9 help
    - issue/PR review

### numpy 2.0 status

- holding pattern for now

### 3.8.4 release

- main reason is for numpy
- waiting for pybind11 to sort some stuff out for 3.8.4rc

### PR review

- twinned axes cursors
   - https://github.com/matplotlib/matplotlib/pull/25556
   - last discussed 8mo ago
   - call likes the examples, will merge when test pass
- internals of autodatelocator logic
   - issue is if one of the levels is empty skip
   - API wise it makes sense to be able to skip levels
   - take propsoed patch, look into fallout in this particualr case off call
- two cyclers
    - we re-export `cycler` from `cycler` and we have a custom wrapper of `cycler` that does extra validation
    - also have a PR that cleans up imports and removes aliases
    - questions
        1. should we still have both?
        2. should we expose either
    - we do not use `plt.cycler` internally
        - is in a whats-new
    - our trend is to simplify so don't import
    - but pyplot should be mostly self-contained and a cycler is useful for setting rcparams
        - set_propcycle will make the cycler for you
        - on net, deprecate
    - consensus
        - deprecate, but be willing to back off if disruptive
- return value of toolbar.save_fig
    - nice way to do this (matches most dialog implementations):
        - `None` -> No file saved
        - SENTENIL -> can't tell if a file was saved
        - happy-path -> string to path
    - implementation (backwards compatible paranoid safe)
        - `None` -> don't know if a file was savef
        - SENTINEL -> actively did not save
        - happy-path -> string to path
    - currently return `None` everywhere
        - proposed implemenatio n
    - one usecase
        - https://github.com/kivy-garden/garden.matplotlib/blob/024d5c47f86577873de0939c169f369dd46ba595/backend_kivy.py#L939-L940\
    - consenus
        - go with the "nice way"
        - make sure API change note is clear that thrid-party backends will have to implement this
        - open an issue with Kivy backend when merged

- branch label rules
    - consenus
        - try it out
        - previously talked about on call and we agreed to do it
        - no user facing impact, low risk and we can always turn it off if we hate it
- bxp tick label revert
    - https://github.com/matplotlib/matplotlib/pull/27916
    - the parameter name and then key in the returned dict no longer match
    - attempt was made to replace dict with DataClass, but gets messy in this case
    - propsoal: 
        - leave bxp_stats alone
        - migrate to something more static in the future
    - consenus
        - go with this
        - also change the docstring to be clearer what it is

### SC timeline
- one week response window then ping once a week

# March 7th
_attending_: @tacaswell, @QWhXj01mSwmTjk5kN1H_qQ (efiring), @rcomer, @ksunden, @story645, @QuLogic, @timhoffm

## Agenda

### old business
- [x] RSE
- [x] 3.9

### new business
- [x] [name=tacaswell] grant updates
- [x] [name=hannah] triage team 

### Issues and PRs

## Notes


### RSE updates 

Kyle:
 - putting is scipy talk propsoal (on dataproto type)
 - data prototype work, thinking about Artist class tree
 - QoL improvements in repo to make less verbose
 - issue and PR review
 - pushing on yet more mac OSX segfaults / objectiveC level exceptions
     - new or pre-existing?  Hard to go back to old versions of OSX so very hard to debug
     - behavior is as documented, but did not notice this behavior before
         - only see when running as a subprocess, test was marked xfail because flaky, lightly tested / under used feature (singleshot timers), test sometimes passes before object crashes
         - subtle interaction with Python GC to produce an invalid pointer
Elliott:
 - Catching up from forced vacation
 - bit more pybind11 work (waiting for cgywin test to pass (just merged!))
 - started to work on performance benchmarks
     - working on windows + arm box

Tom:
 - some issue review + scipy talk discussions

### 3.9 updates

- worked on clearing out milestone yesterday
- no major items that should get a madrush to get in
- RC in 2 weeks
    - how does this interact with numpy 2.0
    - do not hold our RC for numpy beta
    - do another RC as soon as they have an RC
    - hold our 3.9 final for numpy2.0 rc
- david got new pydata sphinx theme working, please look at devdocs due to big changes in upstream themes
    - use social to drive eyeballs at this
    
### numpy 2.0

https://github.com/numpy/numpy/issues/25918#issuecomment-1980214917

- asking for sequence of:
  -  numpy beta
  -  mpl/scipy/... rc (of _something_)
  -  numpy rc
  -  mpl/scipy/... finals (of something)

### grant updates

### triage team

SC needs to be prompt or delegate authority

### repo to hold API automation from social

- good idea, start in @story645 's account and migrate when working


### DST is coming

Remember we follow the German schedule.

### rgba nan handling + extra copies

https://github.com/matplotlib/matplotlib/pull/27848


Conclusion: only copy if we have to mutate the user input

# 29 Feb 2024

_attending_: @ksunden, @QuLogic, @tacaswell, @story645 

## Agenda 

### old business
- [x] RSE reports
- [x] 3.9 progress

### new business

## Notes

### RSE report
- Tom: swamped with other work
- Kyle: 
    - preparing for scipy submissions
    - getting examples in data-prototype working again
    - issue triage / PR review
- Elliott:
    - on vacation
    - made progress on pybind11 work, no PR yet


### 3.9

- Still looking on target for RC in March 
- currently 73 open things in milestone

### numpy 2.0

- things are going slowly
- do micro release when rc to drop upper pin

# 22 Feb 2024

_attending_: @efiring, @ksunden, @QuLogic, @greglucas, @story645 

## Agenda

### Old business

- [x] RSE reports
- [x] 3.9 progress
- [x] scipy tutorial planning

### new business

## notes



### PRs
- [x] [name=hannah] [seperate edgecolor + hatchcolor](https://github.com/matplotlib/matplotlib/pull/26993)
## notes

### RSE reports
- ksunden: macOS, data prototype, general issue & PR review
- qulogic: pr review, finished animation->vid in docs (needs sphinx gallery reviews)

### separate edge + hatch

- setting hatch.color to 'inherit' from edgecolor 
    - needs an API behavior note probably
- use facecolor tracking edgecolor as model 
- on set alpha adjust hatch color? 
    - needs an API behavior note probably 
- setting alpha after setting edgecolor will overwrite current, preserve with users hatchcolor
- Check for parallel behavior, if possible, between Patch and Collection.

### side convo on hatch api
- figuring out which customizations to allow - color, density, etc
    - https://github.com/leejjoon/mpl-pe-pattern-usgs
    - https://github.com/leejjoon/mpl-pe-pattern-monster
- custom registry to allow strings but avoiding naming conflicts 
- similar to MarkerStyle -> HatchStyle
- SDG scope/level project

### pybind11 review
- can we go through w/ one proficient in pybind11 reviewer?
    - can we just get through with "is this ported correctly?"
- benchmarking? 