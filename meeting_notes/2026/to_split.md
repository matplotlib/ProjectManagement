<!-- Template for weekly meeting for quick copy/paste

---

# Month 5th

_attending_:


## Agenda

- [ ] [name=username] - Agenda Item

## Notes

-->

---

# August 20th

_attending_:


## Agenda

- [ ] [name=iccir] - Requesting a brief history of "ToolManager" and "NavigationToolbar2" if we have time.

## Notes


---

# August 13th

_attending_: @iccir, @story645, @ksunden, @QuLogic 


## Agenda
- [x] RSE updates

## Notes

### Data containers
Data container phase:

uniform interface for artists that go in axes 
    - defined by the `describe` and `query` methods
    
- subphase 1: core (artists will use this functionality)
    - reviewer documentation:
        - how to review core and future artists
    - classes ported over from datacontainers/vendored internally:
        - protocol class for containers
            - definition of description
        - `arraycontainer(arrayLike)` 
        - `funccontainer(callable: arrayLike->arrayLike)`
    - minimum version of graph data->viz pipeline 
        - e.g. transfrom edge 
        - theoretically parameters are graph edges are encoding functions 
            - e.g. color
    - single artist: Line2d w/ Line2D data container
        - goal is `query` will take over a lot of what `set_data` is currently used for 
    - helper functions
        - graph building for `data -> axes -> display` transforms 
        - error handling

- subphase 2: extending to more artists types
    - e.g. image, patch, etc 
    - 3d will likely happen in parallel 
    - might be split up by families: AxesImages, Patches, Text, etc.
    - then collections 

- note: delay implementing changes on artist 'til more artists need it 
    - private helper functions when shared by few artists
    - base stuff til all artists are implemented

- subphase 3: extending functionality:
    - more visual parameters: eg color, shape, etc
        - initial is name data fields w/ parameter name
        - needs discussion: how data field->visual parameter associations happen in API
    - semantic containers: e.g. stats like hist
    - downstream containers: e.g. sympy, pandas, 
        - maybe reconcile mpl-data-containers w/ built ins

visual pipeline phase:
- worry about after DC is in

# August 6th
_attending_: @iccir, @efiring, @ayshih,  @scottshambaugh, @QuLogic, @ksunden, @tacaswell, @story645 


## Agenda
- [x] RSE updates
- [x] [name=hannah][32113: 2 reviews for large doc prs](https://github.com/matplotlib/matplotlib/pull/32113)
- [] [name=hannah][29124: plotting section for user guide](https://github.com/matplotlib/matplotlib/pull/29124)
- [x] [name=ayshih][32107: alpha handling when flattening images](https://github.com/matplotlib/matplotlib/pull/32107)


## Notes
### RSE updates
 - Kyle
     - planning around data prototype
         - how we get things merged
     - PR review
 - Elliott
     - short week due to holiday
     - looked at WASM, confused again
     - reviews
         - merged core text
         - reviewing blend modes
     - cartopy
         - waiting on others
 - Tom
     - emails out looking for grant collaborators, starting to hear back

### 2 reviews for large docs 
- fuzzy definition of large docs but will clarify for now
- side discussion on loosening review requirements for code
    - @tacaswell strongly opposed

### alpha
- simplified code and fixed bug 

### blending modes / groups
- Elliott still reviewing

### Mac work
- progressing
- @iccir looked at pybind11 and nanobind and decided that direct binding is still best
    - pybind11 increases binary size
- @iccir will make an issue/project/something listing all the moving pieces

### toolbar icon 
- https://github.com/matplotlib/matplotlib/pull/32095
- needs second review
    
### oxipng
- https://github.com/matplotlib/matplotlib/pull/29925
- waiting on broken github actions + rebase, need to verify new precommit works

### GSOC update
 - discussed simplified scheme for being explicit about layers rather than implicitly extract from the artist tree as discussed on call last week

---

# July 30th
_attending_: @iccir, @tacaswell, @QuLogic, @story645, @ksunden, @scottshambaugh, @timhoffm


## Agenda
- [x] RSE updates
- [x] [name=iccir] macOS backend questions
- [x] GSOC updates (+ Layering API)
- [ ] [name=hannah][32113: 2 reviews for large doc prs](https://github.com/matplotlib/matplotlib/pull/32113)
- [ ] [name=hannah][29124: plotting section for user guide](https://github.com/matplotlib/matplotlib/pull/29124)

## Notes
### RSE updates
 - Elliott
     - cartopy work
         - close to getting an update out
         - some decisons on projects still need to be made
     - GSOC work
     - looking at WASM tests again
         - know what, but not why
 - Kyle
     - paperwork
     - GSOC moving forward
 - Tom
     - tiny bit of review
     - un-pushed work on stub-files for backends

### macOS backend
- have a rework branch that addresses every open issue
- do we want to do a dual release with old vs new
    - merge new + keep old 1/ two cycle deprecation
    - slowly patch in changes across the release cycle
- nothing changes from the user perspective
    - mostly improvements that are better integrations w/ mac 
        - also some blitting improvements
    - no changes to code
- scale of change: 
    - splits out macos backend into obj-c pairs to conform to objc standards, might lose git history
    - figuremanager now a window controller, figurecanvas is now view
    - cleanup event loop
    - will go in as chunked/staged/stacked PRs
- risk/failure modes
    - limited use of matplotlib, might not catch less common use cases
    - worst case is some fancy event/interaction doesn't work
        - remediation is downgrade and wait on bugfix release 
- would maybe need a .mm (objc c++) glue file 
consensus: 
- introduce new backend as macOS, keep old as mac/osx
    - might delete before release,  then wire up aliasing/renaming
        - if we rename the backend, then rename rcparams to new name and keep old name as backends

### GSOC: 
- individual rendering layers, maybe individual renderers down the line
    - marimo does JS rendering on top of mpl rendering
    - zoom boxes is client side rendering
    - better seperation between GUIs and renderer
- render to seperate buffers & then composite buffers
    - layer attribute that ids layer 
    - filter by layer for draw
    - maybe: ```layer = fig.add_to_layer(id, obj(ax))```

Managing the draws:
- before: figure.draw just draws children
- after: build draw tree as groupby layer
    - has a problem w/ artist that draws children in child method
        - possibly some double draws/maybe impart constraints 
        - some explicit subartists some containers of artists
    - parent child currently manages removal & maybe knowing about each other for transform purposes
- alt: maybe as a decorator on draw that filters on layer
    - or as a meta class that modifies draw 

todo:
- patch `fig.add_artist(obj, layer=)` 
    - maybe down the line `ax.add_artist` or threading threw or whatever
    - use this to bypass insertion into draw tree
    - down the line 
- move layering management to figure 


    
# July 23rd
_attending_: @efiring, @ayshih, @iccir, @story645, @ksunden, @QuLogic, @melissawm, @trygve, @tacaswell, @timhoffm 

## Agenda
- [x] RSE updates
- [x] [name=QuLogic] Cairo backends (cf. [#32084](https://github.com/matplotlib/matplotlib/issues/32084))

### PRs & Issue
- [ ] [name=QuLogic] [pybind11 v3 #30291](https://github.com/matplotlib/matplotlib/pull/30291)
- [ ] [name=QuLogic] [std::visit to exhaust std::variant possibilities](https://github.com/matplotlib/matplotlib/pull/30773)
- [ ] [name=ayshih] [path snapping #32018](https://github.com/matplotlib/matplotlib/pull/32018)
- [ ] [name=ayshih] [blend modes, of course! #31162](https://github.com/matplotlib/matplotlib/pull/31162)


## Notes

### RSE updates 
Melissa:
- enforcing that PR templates are filled
    - unfilled templates are usually a strong signal 
    - [shorten PR template](https://github.com/matplotlib/matplotlib/pull/32100)
    - [pr content check](https://github.com/matplotlib/matplotlib/pull/32082)
- poll on discourse about meeting times

Elliott:
- GSOC, midterm evals due 
- 3.11.1 released 
- couple of things came in for 3.11.2
- working on subpixel snapping for markers and AGG stuff

Kyle: 
- GSOC
- [mpl-altair](https://github.com/matplotlib/mpl-altair) -> matplotlib backend
    - instead just do a straight vega-grammer to mpl implementation (akin to [plotnine](https://plotnine.org/))

Tom:
- Scipy

### Cairo fonts
- cairo can't support new features b/c of current API making it so we can't use glyph indices 
    - limitations of toy API
    - choices: 
        - give up on cairo for fonts and use freetypes instead
            - might cause problems with pdfs (selecting text?)
        - mplcairo uses full API instead of toy API, so use this instead 
            - would require an extra install (unless we want to inline this)
            - sticking point was c++ version incompatability which might be resolved 
            - @qulogic long term this is probably the best path forward
- proposal: 
    - deprecate cairo backend
    - special case 'mplcairo'
        - make it an extras `matplotlib[mplcairo]`
    - next step: @qulogic will open an issue w/ proposal to deprecate Cairo

- is cairo worth maintaining? 

tangent: seperate renderer from toolkit 




# July 16th
_attending_: @melissawm, @ayshih, @QuLogic, @story645, Scott Shambaugh, Ricci Adams

## Agenda
- [ ] RSE updates

### PRs & Issue
- [fix for path snapping #32018](https://github.com/matplotlib/matplotlib/pull/32018)
- [fix for mouseover and canvas height #32038](https://github.com/matplotlib/matplotlib/pull/32038)
- [x] [multivar imshow](https://github.com/matplotlib/matplotlib/pull/30597)
   - [x] [Commonize 3D zmargin handling with x and y axes](https://github.com/matplotlib/matplotlib/pull/31287)

## Notes
### RSE updates
- Tom & Kyle - scipy
- Melissa
    - set up and run triage meetings ([Matplotlib Triage Team Guide](https://hackmd.io/@matplotlib/triage) - feedback on this presentation is welcome!)
    - asking for next ideas
    - bringing in meeting notes to meeting
    - Idea: clean up architecture doc PR (tick whatever is done from the todo list)
    - finish up dev docs rearch [26196](https://github.com/matplotlib/matplotlib/issues/26196)
        - Audit style docs/format docs [26392](https://github.com/matplotlib/matplotlib/issues/26392)
    - Audit/summarize automated AI review tools available to see what would fit the repo best. Maybe start with API guidelines
    - Autoclose PRs that don't correctly fill PR template: investigate if this is easy to implement
- Elliott
    - 3.11.1 work - 1? PR left on milestone?
    - cartopy work, waiting on pyproj

### jupyterlite 
- hang up is test w/ fonts slightly different/ WASM issues 
- might be ok w/ pyodide pre-built wheels
 
### 3D margin

- fix either way, question is which margin to use: 
    - keep plots looking mostly the same
    - improves the look
- half the tests get updated 
- major regression change w/ either choice 

### mpl-bench
- devs should have write access

### multivar and z margins
need decisions from @timhoffm 

# July 9th

_attending_: @tacaswell, @ksunden, @ayshih, @qulogic, @story645 

## Agenda
 - [x] RSE updates


## Notes
### RSE updates
 - Kyle
     - general maintence
     - reviewed accessiviz
         - submitted, deadline pushed to July 21 if we want more edits
     - work an dataproto type
     - GSOC
 - Elliott
     - 3.11.1 work
     - review accessivis paper
     - looked at discourse for why mailing list forwarding is not working
         - will think about how to deal with dropped mail
     - cartopy
         - fixed up their tests with 3.11
         - waiting for review
         - 
> [name=hannah] is very grateful for everyone's help
 
- Tom
    - some review
- Meliisa
    - Triage meeting: https://hackmd.io/@melissawm/HysO1VNXMx
### scipy notes
 - next week
     - Tom and Kyle will be there and miss this call
 - need to write tools plenary
     - hit font work
     - advertise triage team/NCM meetings
     - tease alpha blending

### Blend modes
- can support fancy blends in vector backends that do not natively supported 
- not supported means no clear path to implementation
- most likely done

### docs milestone
needs to be manually published, should either automate or drop


# July 2nd
_attending_: Scott Shambaugh, @ksunden , @tacaswell, @QuLogic , @timhoffm , [@anntzer](@pXw4hSgTQF2--OciPYwa1w),  @story645, 

## Agenda
- [x] RSE updates
- [x] 3.11.1 ?
- [x] [name=hannah] [accessviz](https://github.com/story645/accessviz) due July 8th
- [ ] [name=scott] [3d offsets](https://github.com/matplotlib/matplotlib/pull/31279)
- [ ] blend mode PR

## Notes
### RSE updates
 - Kyle
     - working on plan to review data prototype and prep
     - GSOC
 - Elliott
     - GSOC
     - working on cartopy
     - 3.11 looked at pdf subsetting
         - there is subsetting bug in PDF (reported as surprise ligature)
 - Tom
     - minor review
     - dealt with a privacy disclosure
### 3.11.1
- no emergency
- aim for next week

### acessiviz 
- Kyle, Tim, and Scott will look at

# June 25th
_attending_: @ksunden @tacaswell @QuLogic @efiring @story645 @ayshih @scott shambaugh

## Agenda
- [x] 3.11 fallout
- [x] RSE updates
- [ ] blend modes

## Notes
### 3.11 fallout
 - some minor regressions, mostly fixed


### RSE updates
- Kyle
    - looking at data prototype stuff
    - some review, helping with 3.11
    - still looking at gif read failure on azure
        - one failure on one azure job on windows reading a baseline gif
- Tom
    - mostly swamped with other stuff
- Elliott
    - 3.11 followup
    - GSOC
    - looking at cartopy release prep



# June 18th
_attending_: @ksunden, @melissawm, @QuLogic, @ayshih, @story645, @trygve

## Agenda
- [ ] RSE
- [ ] GSOC
- [ ] 3.11
- [ ] PR review
    - [Add path.sketch_seed to control sketch randomness #31311](https://github.com/matplotlib/matplotlib/pull/31311): API design decision

## Notes

### RSE
- sphinx-gallery implemented tags, @melissawm will investigate transtion
    - tagging as sprint activity
    - @ayshih : SunPy is using this new functionality (in fact, it was developed under SunPy OSTFL funding), and here's an [example page](https://docs.sunpy.org/en/latest/generated/gallery/plotting/index.html) that shows how tag filtering works
- 3.11 has been out for a week 
    - 3.11.1 planned out soon

@QuLogic: 
- investigating 3.11 bug reports
- fixing type hints
- helping w/ cartopy release
- gsoc

@ksunden:
- review, gsoc, data-prototype
- debugging failing windows test

@melissawm:
- deactivated inclusion of items in new contributor board 
- consolidated dependency(dependabot) labels
- started triaging backlog
- [Add path.sketch_seed to control sketch randomness #31311](https://github.com/matplotlib/matplotlib/pull/31311): API design decision
    - Needs verification that tests are implemented correctly, not just an API decision.
    - Might be a good sprint task?

### Path.sketch_seed
- most of the review work is checking that the tests check what they're supposed to 
- API decision of seperate parameter or extend sketch to 4 tuple
    - reason for seperate was mostly b/c implementation for seed management is independent of sketch

### GSOC

- Tue/Thu schedule to assign tasks and onboard contributor into MPL draw stack.

---
# June 11th
_attending_: @efiring, @tacaswell, @QuLogic, @ayshih, @ksunden, @story645 

## Agenda
- [x] RSE
- [x] GSOC
- [x] 3.11


## Notes
### Scipy / JDH lunch discussion
- [x] @story645 will send email to our dev list soliciting stories / memories

### RSE
- Tom
    - very little mpl last two weeks
- Kyle
    - GSOC
        - found an issue to add pre-draw event in our event system
    - still working on data-prototype PR
- Elliott
    - closed the 3.11 milestone
    - ball is rolling on doing final release
        - PR reviewed, tag locally


# June 4th
_attending_: @efiring, @ayshih, @ksunden, @story645, @scottshambaugh, @melissawm, @timhoffm, @QuLogic, @trygve


## Agenda
 - [x] RSE updates
 - [x] GSOC updates
 - [x] 3.11
 - [x] Multivariate colorbars – https://github.com/matplotlib/matplotlib/pull/31214

## Notes

### RSE
- [name=Elliot] 3.11 prep, docs/review
- [name=Kyle] 3.11 review, gsoc, data prototype
- [name=Melissa]
    - https://hackmd.io/@matplotlib/triage
    - Updating some labels?
    - https://github.com/matplotlib/matplotlib/pull/31479
    
### New contributor meeting
- make next one triage focused
    - explain labels
    - discuss patterns for finding issues
    - walk through triage
- have more advert roll out
- use structured presentations:
    - [Matplotlib Triage Team Guide](https://hackmd.io/ldtuYHHXSOmyXhdprUM7rg#/)
    - [How can you contribute to Matplotlib?](https://hackmd.io/zdaQtgq0QsWjm95TSMw0YA#/)

### GSoC
- discussion in https://discourse.matplotlib.org/chat/c/gsoc/21
- work-log: https://hackmd.io/DIYP5uqhSi6D2ek4E8ObsA
- on going task: design work on where the bookeeping happens for overlay

### multivariate
- rebase and merge [multivar imshow](https://github.com/matplotlib/matplotlib/pull/30597)
- rebase colorbar PR onto imshow 
    - needs review 

### 3.11
- [update sphinx theme](https://github.com/matplotlib/matplotlib/pull/31539)
- [reduce duplicates in contributor stats](https://github.com/matplotlib/matplotlib/pull/31815)
- 

# May 28th

_attending_: @tacaswell @efiring @ksunden vikash @QuLogic @story645 @timhoffm 

## Agenda
 - [x] RSE updates
 - [x] GSOC updates
 - [x] 3.11
 - [ ] GSOC kickoff

## Notes
### RSE updates
 - Kyle
     - review for 3.11
     - getting back onto data-prototype work 
     - starting to ramp up GSOC
 - Tom
     - mostly not
 - Elliott
     - 3.11
         - finished off docs
         - posted update on downstream testing, can probaly close downstream tracker issue 31589
         - need to commit guide on how to deal with text test image changes
         - some outstanding 3D bugs , have PRs for them
             - examples from third-party examples with 3D looked ok
     
### GSOC
- intros
- what is the project
    - overlay API for Matplotlib
    - this in the first call
-todo: write short/pro-con on two approaches:
    - layer concept inside figure (managed in draw)
    - layer concept outside figure, (calls figure draw as part of managing layers)

### 3.11
- final within a week
    - waiting on 3D + review of whats new

# May 21st

_attending_: @tacaswell @QWhXj01mSwmTjk5kN1H_qQ @ksunden @QuLogic @story645 @ayshih 

## Agenda
- [x] RSE updates
- [ ] PR review
- [x] 3.11 status

## Notes

### RSE

- [name=melissa] (will join at the second half hour!) PRs waiting for review/decision:
    - [DOC: Update triage team nomination instructions#31089](https://github.com/matplotlib/matplotlib/pull/31089)
    - [Add template for new triage team invitation#47](https://github.com/matplotlib/governance/pull/47)
    - [MAINT: Set "skip internal contributors" to PR welcome bot#31479](https://github.com/matplotlib/matplotlib/pull/31479)
        - There is a current bug upstream but even when fixed I think it's a good idea to have this option set to true, which means creating the `GH_PAT_READ_ORG` secret.
        - Another option is to close this PR and try to detect first-time-contributors from the triage board.
 - Tom: swamped with other things
 - Kyle:
     - mostly review
     - did spot check of recent pushes for malicious commits
     - hardened some of our "do not push to branch with out PR" settings
 - Elliott
     - slow week (long weekend)
     - through fedora rebuild and it appears all issues (other than image changes due to text) addressed
     - waiting on docs update

### 3.11
 - in home stretch, see Elliott's notes above

### PR review
- blend mode PR https://github.com/matplotlib/matplotlib/pull/31162 
- https://github.com/matplotlib/matplotlib/pull/31703 the joys of floating point
- reviewed triage team, will merge tomorrow
- invite template in review process
- wait on bug upstream for new-contirbutor bot and look at alterantives / pinning back.

---

# May 14th

_attending_: @efiring, @ayshih, @QuLogic, @ksunden, @story645, @timhoffm 

## Agenda
- [x] RSE updates
- [ ] PR review
- [x] 3.11 status
- [ ] [name=hannah][Accessviz](https://ieeevis.org/year/2026/info/program/workshops/#accessible-vis)
    - 3rd Workshop on Accessible Data Visualization
    - due mid july (?)
    - seeking feedback/co-authors: [draft](https://github.com/story645/accessviz)

## Notes
### RSE 
- RC2 released Tuesday 
    - fixed seaborne related tests failures
    - cartopy CI indicates fixed CI
    - @QuLogic prepping release notes
- @ksunden review + data prototype (mostly review)

### 3.11
- few test issues left, likely ghostscript related 

### accessiviz
- thesis: architecture/design decisions facilitates acessibility 
- modeled on [bokeh accessibility audit](https://bokeh-a11y-audit.readthedocs.io/)

### Blend mode and blend groups 
- https://github.com/matplotlib/matplotlib/pull/31162
- blend mode 
    - blends to below based on z order
- blend group which fixes bugs
    - blend artists by groups
    - needs renderer calls - open/close_blend_group

- `ArtistGroup` helper function for plotting layer
    - usually users don't call renderer directly
    - calls draw on group w/ blend mode, result then gets added to draw stack

    - can this be spun into it's own thing for all things grouping artists
    - this PR leaves `ArtistGroup` as example, spin off `ArtistGroup` as API as a standalone PR

- How are artists currently grouped?
    - collection of `same` Artist
    - container of `different` Artists 
    - potential: compound Artist for semantic groupings
        - PieContainer if it had a draw method
    - > [name=hannah] we should document this in architecture docs 
     
# May 7th

_attending_:  @efiring, @timhoffm, @rcomer, @ayshih, @ksunden, @QuLogic, @story645, @tacaswell 

## Agenda
- [x] RSE updates
- [x] PR review
- [x] 3.11 status
    - [x] [PolarTransform `apply_theta_transform` deprecation](https://github.com/matplotlib/matplotlib/issues/31624)
    - [x] [3.11 rc issues](https://github.com/matplotlib/matplotlib/issues/31589)
- [ ] (if time permits) Triage
    - [ ] [#31346 - Disable auto-loading custom matplotlibrc files](https://github.com/matplotlib/matplotlib/issues/31346)

## GSOC
- not starting til after May 20th, 
- google granted 16 week extension, 1st eval moved to July 20th

## RSE
- 3.11 finalizing + release notes
 
## 3.11 RC issues
- reported upstream: myst-nb, animatplot, iplotx, mapclassify, scalebar, pytest-mpl
- @qulogic put in pr for seaborn + #31590
- #31624 PolarTransform
    - deprecate vs. delete?
        - set true/none triggers warning to set to false
        - false currently fails silently (is what set in docs)
    - currently half deprecated, should it be full? 
        - yes, make it full deprecration

## auto-loading custom matplotlibrc
- disable autoloading for security reasons 
- options:
    - add another option to matplotlibrc environment variable
    - add turn off  flag "MATPLOTLIBRC_UNSAFE_CWD=1"
    - pro: easy to document 
    - con: creates coupling btw/ MATPLOTLIBRC \which takes filepath) * and  MATPLOTLIBRC_UNSAFE_CWD
    - USE/NOT USE takes priority

deprecation path: go through current list, report list and warning that in future must be listed explicitly 

consensus: add empty flag to current RC


# April 30th
_attending_: @ksunden, @QuLogic, @ayshih, @trygve, @story645 

## Agenda
- [ ] RSE update
- [ ] PR review
- [ ] 3.11 status
    - [ ] [3.11 rc issues](https://github.com/matplotlib/matplotlib/issues/31589)
    - [ ] [Expire some missed deprecations from 3.9](https://github.com/matplotlib/matplotlib/pull/31588)
    - [ ] [Should `_make_axis_parameter_optional` handle `None`](https://github.com/matplotlib/matplotlib/issues/31590)
- [ ] (if time permits) Triage

## Notes

### RSE updates:
#### Kyle & Elliott
- 3.10.9 + 3.11 RC out
    - dealing w/ the bug reports 
#### Kyle
- contracts and backend things
#### Elliott
Fedora as proxy for general problems:
- found 10 failures
- reporting to downstream projects
-Release Critical: decide what to do w/ `make_axis_ parameter` 
    - seaborn passes a string into `scale` for the axis argument, but axis is never used so it's ignored. eventual goal is maybe to remove/deprecate. 
  - since seaborne doesn't pass in an axis, is not ignored and blows up
  - raises ambiguity w.r.t. first parameter 
- will probably do a second RC to check if issues are resolved
needs decisions/to be in by next RC
- expiring  deprecations (needs review)
- make_axis_parameter 

#### Melissa

- The triage team nomination instruction PR is I think ready: DOC: Update triage team nomination instructions by melissawm · Pull Request #31089 · matplotlib/matplotlib · GitHub
  - will review the current template used to invite new maintainers and potentially reuse it for triagers
- will update the reviewer guide to include a note about when to stop reviewing low-effort PRs. 
- will also include a link to the new triage board.
- If you have other suggestions for tasks or activities please let Melissa know. Thanks!

#### after 3.11 triaging
- alpha blending
- multi-variate colorbar 
 

#### GSoC
@story645 will email accepted person to kick off community bonding

---
# April 23rd
_attending_: @tacaswell, @efiring, @QuLogic, @ksunden, @story645, @ayshih, @timhoffm, @melissawm 

## Agenda
- [x] RSE update
- [ ] PR review
- [x] Feedback on new triage board: https://github.com/orgs/matplotlib/projects/11
- [x] 3.11 status
- [ ] (if time permits) Triage

## Notes

### RSE updates
- Kyle
    - GSOC list in, just ranked one choice as we can only take one
    - going through release checklist for 3.10.9 today, will be tagged after meeting
- Tom
    - mostly BNL stuff, project management / paperwork
- Elliott
    - getting through 3.11 PRs
    - all PRs in
    - fixed website
        - internal cert expried between DO and CF
    - [#23616: mathtext support underline](https://github.com/matplotlib/matplotlib/pull/23616#issuecomment-4230062034)
        - accept trade off of sometimes looking great/terrible over  consistently looking ok

### 3.11
- one last PR (underline one discussed above)
- branch today !
- first one for Elliott using new (seperate repo) process

### Triage
- once a consensus is reached on thread, @ksunden and @QuLogic can add person 
    - what is consensus? what is the timeline?
        - leave nom up for a week, if nobody opposes we accept
        - email invite template - whoever can add people to theme
            - add label email sent
            - close thread when they accept/reject
- [Nomination instructions PR](https://github.com/matplotlib/matplotlib/pull/31089)

### new board
- Caswell thinks it looks great
- @melissawm will check w/ upstream on whether the board can be customized or we need to fork to customize
- user merged rather than closed? 
- bot detection 
- retire first time contributor board bt merging into triage board
- add new view for approved unmerged w/ flakey tests

### [privatize formatter attributes](https://github.com/matplotlib/matplotlib/pull/31416)
- track internal state so shouldn't be user modifiable 

# April 16th
_attending_: @QuLogic, @efiring, @ksunden, @tacaswell, @story645, @timhoffm 

## Agenda
- [x] RSE update
- [x] fonts
- [x] other 3.11
- [ ] PR review
    - [ ] Changing 'animation.html' to [make `Animation._repr_html_` more useful](https://github.com/matplotlib/matplotlib/pull/31510)

## Notes
### GSOC applicate notes and down selection
(not taking notes for obvious reasons)

### RSE update
- Kyle
    - looked at flaky tests
        - startup time of subprocess was longer than we thought
    - some review
    - GSOC review
- Elliott
    - publicized the nightlys coming
    - seeing some people update their test images, but have not complianed
        - Albert may have handled at least 2 of these so know it was coming and all the details
    - also worked on the flaky test
    - put is PR to fix pybind11 failure
    - GSOC review
- Tom
    - got ROSE 2020 grant final report
- Melissa via staff chat
    - MAINT: Add PR triage board action by melissawm #31499 
    - DOC: Update triage team nomination instructions by melissawm #31089 
    - following up on the triage team nominations - what are the next steps here?


### font

nothing came up

### other 3.11

- giving some time for nightly complaints
- branch today, aim for RC on Tuesday
- outstanding PR on setting image styles
    - kept default as None, raise deprecation warning that it's changing to mpl20
- ran through a bunch of PRs

### 


---
# April 9th
_attending_: @ksunden @QuLogic @scottshambaugh @efiring @ayshih @timhoffm @melissawm 

## Agenda
- [x] RSE update
- [x] fonts
- [ ] other 3.11
- [ ] PR review
- [x] [name=hannah][use minigallery on tutorial landing page](https://github.com/matplotlib/matplotlib/pull/31275)
    - needs a yes/no: replace hardcoded html thumbnails w/ minigallery directive 

## Notes

### RSE Updates

- Kyle:
    - 3.11 review
    
- Elliott:
    - 3.11 PRs
    - looking at some doc build speedup

- Melissa: 
    - Fix for first-contribution action: https://github.com/matplotlib/matplotlib/pull/31479
        - Melissa to report upstream and we'll give it 2 weeks to see if an actual fix is merged.
    - Triage board: can anyone with permissions create a GitHub app for the Jupyter Triage Board? https://github.com/jupyter/pr-triage-board-bot#set-up
        - (I can probably take care of duplicating the board and setting the rest of the items up, but I can't create an org app)
        - Kyle to set this up and communicate back with updates.

### Minigallery (31275)

- PR summary needs re-writing
- PR is an improvement, worth merging
- Elliott to take care of merging after meeting

### GSOC
- Kyle & Elliott have started looking at the applications, dividing into subject categories. Two biggest are the transform (11) and the overlay (15).
- schedule meeting to select top few

## Triage (if there's time)

- [ ] One approval: [Adds plot_exclude_patterns config to selectively disable plot_directive.#31270](https://github.com/matplotlib/matplotlib/pull/31270)
- [ ] Needs review: [[BUG] Fix alpha bug on 3D PathCollection plots.#25478](https://github.com/matplotlib/matplotlib/pull/25478)
- [ ] Very old, needs review/decision: [Let twin-axis aligned at the specified position#26109](https://github.com/matplotlib/matplotlib/pull/26109)
- [ ] Recent, needs discussion/decision: [Fix #21409: Make twin axes inherit parent position#31353](https://github.com/matplotlib/matplotlib/pull/31353)



---

# April 2nd
_attending_: @ksunden @QuLogic @tacaswell, @ayshih, @efiring 

## Agenda
- [x] RSE update
- [ ] fonts
- [ ] other 3.11
- [ ] PR review

## Notes

### RSE updates

- Kyle
    - slow week, some travel and out of pattern
    - have 41 GSOC applications
        - 10 for indirect transfrom
        - 14 for overlay
        - rest are misc
- Tom
    - took 3 of 5 last work days off 
- Elliott
    - PR review, lots of small PRs while waiting for big PRs to land.
    - some new font fetures (maybe not for 3.11)
    
### fonts!


# March 26th
_attending_: @ksunden, @melissawm, @ayshih, @scottshambaugh, @efiring, @QuLogic, @story645, @tacaswell @timhoffm   

## Agenda
- [x] RSE updates
- [x] 3.11
- [x] setuptools scmscm
- [ ] first time contributor review

### RSE updates
- Kyle
- Elliot
- Melissa
    - discussion about reducing number of open PRs
- Tom
    - Y2 funding from NASA is with NF

### 3.11
- text things need review and merge

### setuptools-scm
- 10.0.2 broke all of our tests
- we should pin to less than 10 for now
- sort out if we need to do our own thing 
    - https://discuss.python.org/t/please-make-package-version-go-away/58501
- only a dev dependency so not too worried about pinning

### eval patch
- we should backport to 3.10.9 and make sure there is a release note
- pick one or the other for recursing when handling args/kwargs
    - will go with recurse on both

# March 19th
_attending_: @ksunden, @QuLogic, @tacaswell, @melissawm, @ayshih, @story645 
jetbrains: Natalia, Galina
## Agenda
- [x] Jetbrains styles
- [ ] RSE update
- [ ] 3.11
- [ ] PR 

## Notes
### Pycharm styles 
- 2 new styles - light/dark.
    - paired light + dark 
    - 10 colors in a cycle
    - cvd friendly, + accessibility
    - made by a designer 
    - manage updates - add version # 
    - licensing: no intent to limit the schemes 
### RSE updates
- Kyle
    - doing backports to 3.10 for some security hardening
    - review for 3.11
- Elliott
    - going through open PRs and clear them out
    - now have WASM ci to produce nightlies for py312
        - py313 broken for reasons we don't understand and don't got pypi
    - jupyterlite docs being looked at again
        - we can now run the devdocs against these wheels
    - font stuff
        - updated the font height PR
- Tom
    - mostly vacation
- Melissa
    - 3 PR open that need review
        - [minor formatting and linting issues](https://github.com/matplotlib/matplotlib/pull/31338)
        - [triage team nom process](https://github.com/matplotlib/matplotlib/pull/31089)
        - [focus on one pr](https://github.com/matplotlib/matplotlib/pull/31329)
    - invitation to discuss triage with Melissa
        - Feel free to book at time with me at https://calendly.com/melissawm/chat

### 3.11


# March 12th
_attending_: @tacaswell, @efiring, @QuLogic, @ksunden, @trygve, @scottshambaugh, @story645 

## Agenda
- [x] Security issues
- [x] RSE updates
- [x] 3.11
- [ ] PR review


## Notes


### RSE updates
- Tom:
    - just review work
    - found pybind11 regression on their main
- Elliott
    - 3.11 prep
        - finished off text metric work (should be last thing!)
- Kyle
    - mostly 3.11 prep
    - going thorugh at PRs with atleast 1 approval (particuarlly Elliott's)
- Melissa
    - autoclose tag name
        - current needs XXX not clear enough
        - proposal from Caswell: "autoclose candidate"
        - Hannah / Melissa should just make a choice
    - updates to new contributors PR table (gh project)
    - thinking through exact process for handling triage team nominations so we do not lose track of things in flight

### Security issues
- Security policy: https://github.com/matplotlib/matplotlib/security/policy
- How much should we handle these in public? Is there a private channel for this? Role of Tidelift? 
    - please report things that should be confidential through tidelift
    - this does send emails to the team, only gotten spam so far so haven't "stress tested" the process yet
- Always backport security issues? GH tag?
    - depends on severity
- for the current set
    - more hardening than vulnerabilities, backport to 3.10.x
    - scott has 1-2 more to submit

### 3.11 status
- only fonts left and hardening PRs
- would be good to land a few more performance PRs
- fontmetric PR
    - https://github.com/matplotlib/matplotlib/pull/31291/
    - consenus of call is that single line does not need line spacing 
- https://github.com/matplotlib/matplotlib/pull/31281

### PR review
- 

### triage/maintainers/discourse
- Orphan PR cleanup
- [name=Melissa] First-time contributors PRs project: https://github.com/orgs/matplotlib/projects/1/views/3
    - Recently updated. If you feel like it, take a look at some of the "Needs decision" PRs.
- [name=Melissa] Autoclose bot: https://github.com/matplotlib/matplotlib/pull/31283
    - Can we agree on the label name? 
- [name=Melissa] Triage team nominations: https://discourse.matplotlib.org/c/development/private-discussion-about-nominations-to-the-triage-team/23
    - Next steps?


# March 5th
_attending_: @tacaswell, @efiring, @timhoffm, @melissawm, @scottshambaugh, @ksunden, @ayshih, @story645, @anntzer

## Agenda
- [x] more AI related fallout
- [x] RSE updates
- [x] 3.11
- [ ] PR review


## Notes
### adopt some of np's wording for new contributor message
- adding a "why here?" to the pr greeting bot for new contributors
    - NumPy wording: https://github.com/numpy/numpy/pull/30932/changes
- 
### RSE updates
- Kyle
    - scipy tutorial proposal
    - PR review for 3.11
- Tom
    - minimal
- Melissa
    - New contributors meeting - students from Portugal
    - [Remove gitter from docs](https://github.com/matplotlib/matplotlib/pull/31236)
    - [DOC: Update triage team nomination instructions#31089](https://github.com/matplotlib/matplotlib/pull/31089)
        - Discussion: Triage chat on Discourse?
    - Looking into https://github.com/matplotlib/matplotlib/issues/31108
    - Next: autoclose bot
 - Elliott
     - font stuff

### 3.11 status
- https://github.com/matplotlib/matplotlib/issues/31220  (linesize)
    - historically the height of lines was to measure height of `lp`
        - maybe actualy text as for taller things
    - this is not reliably as it is possible to have fonts without either an l or p (e.g. emoji, CJK)
    - can ask the fonts directly for the size rather than use heur
    - istics
        - but this will change tests
    - thearding this through the backend API is a big lift
    - accepted propsoal: hard-code the answers for the default font (dejavu) for 3.11 so the tests do not change when we implement this in the future
        - con: bit brittle
        - pro: prevents us from needing major changes

### PR review    
- Alpha compositing [#31162](https://github.com/matplotlib/matplotlib/issues/31162)
   - [alpha blending modes](https://hackmd.io/d4jJmDiKR2G4DAM4nVZTtA#Alpha-compositing)
   - currently renderer level, matches the API style of agg filters
   - do not try to thread this through main plotting API
   - concern about re-using/co-opting `rendered.{open,close}_group`
   - this provides compositing groups
       - if drawing artist with alpha on an existing background using
       - there are other compositing modes, but do not want to do globally
           - really want to render a subset of artists together with the other mode and then composite that whole thing into one
   - discussion about pulling blending groups out into their own functions
   - some concern about dealing with interleaved blend and filter groups in Agg but we think that this is tractable with 

- [name=Scott] A few ready-to-go PRs with one review (thanks Tim!) that need one more. No rush, just highlighting:
	- Bugfix https://github.com/matplotlib/matplotlib/pull/31061
	- Performance https://github.com/matplotlib/matplotlib/pull/31005
	- Performance https://github.com/matplotlib/matplotlib/pull/31004
	- Performance https://github.com/matplotlib/matplotlib/pull/30995
	- 3D log axes https://github.com/matplotlib/matplotlib/pull/30980

### triage/maintainers/discourse
- public discourse channel 
- private triage + maintainers team + channel
    - [x] move triage nomination to this category
    - [x] traige, maintainer teams added to discourse

# Feb 26
_attending_: @efiring, @rcomer, @tacaswell, @ayshih, @ksunden, @melissawm, @timhoffm, @scottshambaugh, @story645, @QuLogic, Ammar Sharif (@Ammar Sharif)
## Agenda 
- [x] RSE
- [ ] 3.11
- [x] [name=hannah] change chat links to discourse
- [x] [name=hannah][autoclose bot](https://github.com/matplotlib/matplotlib/issues/31164)
- [x] [name=hannah][moderator guidelines](https://github.com/matplotlib/matplotlib/pull/31200) 
- [ ] review https://github.com/matplotlib/matplotlib/pull/31021

### PR review


## Notes 

- RSE updates
    - Melissa
        - Working on https://github.com/matplotlib/matplotlib/pull/31089
        - Reviewing triage team nominations
        - Reviewing more PRs
        - Met with Tim to discuss triage
    - Tom
        - minor paperwork and issue review
    - Kyle
        - issue review trying to get 3.11 out the door
        - planning a tutorial for scipy
    - Elliott
        - sick last week, not super productive
        - font work
        - preparing issues for tracking work for follow on

### chat on discourse

- should we cut over?
- seems to be going tell

decision: lets cut over!

- Melissa will submit PR to update links

### 3.11

- doing OK, last minute mathtext threw monkey wrench in
- need to land one more PR that changes test images, can delay features to next version
- RC target next week
    - two or three PRs to clean up images
    - should we move tests to new style?
- request to get #31021 in for 3.11
    - yes

### autoclose bot

- we put a label onlow-quality PRs
    - bot posts instructions on how to get reviewed
    - bot auto-closes if no after a week or so if no feedback
- possible use https://github.com/2ndSetAI/good-egg to flag score/reputation of contributor
    - some concerns about posting a public behavior report to an issue
    - if we do this should put it someplace private that auto posts
    - a services that we put a GH handle into and get a report
    - a bot that flags on someting very simple like "more than 50 opened PRs in last week"
    - use new-contributor project board

going to go with:
 - trigger this to new contirbutor board -> Melissa will work on this
 - turn on bot with 2 week timeout

### moderator guidelines
- violates our contribution guidelines 
- enforcement:
    - three verbal warnings (temp ban an #3)
    - temporary ban
        - three more verbal warnings?
    - when people come back from temporary ban, unlikly a second temporary band will help
        - if behvior persists/doesn't improve, then escalate 
    - consult in chat as needed
- bring both temproary and permenant bans to this meeting for awareness
    - we should comment on issue anyway
- platform specific bans, ban from all is CoC
- AI can just be banned b/c it's not a person w/ feelings

### image placement: [31021](https://github.com/matplotlib/matplotlib/pull/31021)

# Feb 19
_attending_: @tacaswell, [@efiring](@QWhXj01mSwmTjk5kN1H_qQ), @timhoffm, @ksunden,  @scottshambaugh, @ayshih, @rcomer, @melissawm, @guenp, @story645  
github: Camilla Moraes (@, Abigail Cabunoc Mayes (@abbycabs), Sarah Kaiser, Ashley Wolf (@ashleywolf, mrjf 
numfocus: Arliss 

## Agenda
- [ ] AI agents 
- [ ] RSE updates
- [ ] 3.11

## Notes 

### AI agents
- please don't take down @crabby-rathbun, for historical records
- labeling accounts as AI/Human
    - would be nice to know if the code is human generated
    - github has a bot flag, but used more for automation 
    - at which level? account, post, both? 
- clarify that user bears responsibility for their agents in TOS
- unclear expectations around guardrails for copilot
- surface Ai policy/agents.md as community health type documents (like license.md)
    - setting expectations around AI use
    - no standard for agents.md contents yet, github might be able to set one
- managing pr allowances/restrictions 
    - allow lists/chains of trust
    - moderation levels/roles 
    - - adding people efficiently 
- efficacy of reviewing/dealing w/ random agentic PRs
    - maintainers can use agents too
- enforce contributing guidelines that the bots need to follow
    - github has an AI tool for reviewing incoming contributions based on contributions guidelines
- two problems
    - good actors - follow agents.md, etc, 
    - bad actors -  ignore agents.md, etc, 
- rate limit accounts scaled by account age/reputation
- requiring issue before PR
    - agents are looking for issues - require issue assignment to open PR
    - manually assign people to allowlist?
    - roles can bypass this gate

### RSE updates

- Melissa
    - Working on https://github.com/matplotlib/matplotlib/pull/31089
    - Reviewing triage team nominations

# Feb 12
_attending_: 
[efiring](@QWhXj01mSwmTjk5kN1H_qQ), @ksunden, @tacaswell, @melissawm, @story645, @timhoffm, @scottshambaugh, @trygve, @ayshih, @julian p (gh), 

## Agenda
- [ ] RSE updates
- [x] abusive AI agents
- [ ] 3.11


## Notes
### RSE updates

- Melissa
    - Met with Albert to gather impressions on onboarding, documentation and the triage team expectations in general
    - Will use results also to finish up https://github.com/matplotlib/matplotlib/pull/31089

### Abusive AI

https://github.com/matplotlib/matplotlib/pull/31132

 - can we block
     - probaly not easily, if it is using api / gh cli tool to do this
     - is this against GH ToS?
         - @melissawm did report this as spam/inauthentic activity
 - can we speculate on the motivation of the human in the back?
     - probably not
     - probably does not really matter
 - how do we deal with AI agents?
     - on level is a human doing copy/paste to the agent
     - fully autonomous just go do stuff
 - code generation
     - in pre-AI code generation was expensive, so we work together to generate code
     - add effort in PR review to gatekeep / keep quality up
     - now code generation is super cheap, but review is still expensive
     - thing we want from contributors is their thoughts and expericances
     - if we want to take AI code to code base, should have core developers drive the agents
         - more efficent, cuts down review loop
 - LLVM has good language for this
     - "extractive contributions" https://llvm.org/docs//AIToolPolicy.html 
 - explain that gfi is training [#31142](https://github.com/matplotlib/matplotlib/pull/31142)
 - do we want to do any media prep?
 - asks for GH?
     - rate limit new account to opening new PRs / number of total open PRs
     - add a flag to the user account when they have done spammy / verbose thing
     - does the blog violate GH ToS
     - can add requirement to flag AI generated as such
 - looks like there was another issue involved that commented, had a comment hidden, and is now completely gone
     - may GH deleted the account / comments?
 - analogy to classes using us in classes
     - we are getting used as unpaid, involentary test subjects
     - cheap for agent owners, expensive for projects
 - fully automated PRs are effectively DDOS attacks on projects
 - seems like this is coming up everywhere at at same time (numpy/scipy, napari, scienitific pyhon, ...)
 - https://github.com/matplotlib/matplotlib/pull/31026 merged to get clearer rules in
 - keep these rules framed as being about maintaining the health of the project over the long term
     - looks like there is going to a continium of human and machine interaction
 - AI seems to work surprisingly well
     - but you need to know what you are doing to make good use of it
 - limit AI/LLM for GSOC
     - we should make clear that the "get to know you PR" should be done with brain
     - concerns about full ban on AI for english as an additional language speakers
     - add wording that we expect authentic engagement
     - make clear AI is a tool and we want your efforts / thoughts

# Feb 05
_attending_: 

[efiring](@QWhXj01mSwmTjk5kN1H_qQ), @ksunden, @tacaswell, @melissawm, @story645, @greglucas, @timhoffm, @QuLogic, @scottshambaugh, @ayshih,

## Agenda
- [x] RSE updates
- [ ] 3.11 updates
- [ ] context menus vs menu bars
- [x] [name=hannah] GSOC
- [x] move away from pre-commit to prek


## Notes
### RSE updates
- Melissa
    - Hannah created the Discourse category https://discourse.matplotlib.org/c/staff/private-discussion-about-nominations-to-the-triage-team/23
    - Created PR to fix new contributor bot: https://github.com/matplotlib/matplotlib/pull/31090
    - Created PR to fix docs on triage team nomination instructions: https://github.com/matplotlib/matplotlib/pull/31089
- Tom
    - mostly paperwork, some review
- Kyle
    - PR review, moving 3.11 along
- Elliott
    - mostly font things
    - cleaned up docs server
        - a big and un-useful space was the dev-docs
        - tried tuning the reflog / gc on all of the repos
- Greg
    - no work
    
### move away from pre-commit to prek
- https://github.com/matplotlib/matplotlib/pull/31081
- faster to setup, runtime about the same

### GSOC
soft-missed the NF deadline, but try anyway:
- https://github.com/numfocus/gsoc/pull/565

projects to propose:

- pull "relative" transforms out of annotate
- ~pull all style information into a dataclass hanging off the object (aligns well with dataprototype)~ too much design work
- add a first-class "overlay" layer API for interactive backends
- leave "choose your own adventure"

### context menu vs menu bar
- https://github.com/matplotlib/matplotlib/pull/30976
- add the ability have a right-click context menu
    - concern is that users have already added their own context menus and we need to be careful about breaking user
    - also concern that right-click is not availble on all platforms
- next idea was to move everything to the menu bar
    - discovered issue: how does this map to sub-plots
        - "magic wand" like pan/zoom
        - dropdown menu of subplots (may be confusing with badly named subplots)
        - broadcast to all applicable subplots
        - rely on current axes
- if we have overlay infrastructure can do "hot corners"
- do "locked and discrete" motion (like x/y lock pan/zoom)
    - we have roll now through mouse so might be hard
    - hold control to snap to nearest 5 deg on top of current rotation
- add something like the blender gizmo in corner, put into that
- add "turn on context menu button" to menu bar
    - works, but awkward user experiance
- put into the Qt plot updater
    - propbly would require porting to atleast tk and macos
- could take the position that if we create the figure window we can control the context menu
    - maybe go with this option with:
        - rcparam and API to turn off all together
        - detect if the user registers a right-click and remove ours + warn (with knob to supress the warning)


CONSENSUS
 - try menu that turns itself off on detecting conflict
 - create issue to snap 3D navigation anyway


### very fast fonts
- re-review 31046 now matches the constasts from LaTeX
- https://github.com/matplotlib/matplotlib/pull/31046#issuecomment-3846257438 is the font people will see the most, but latex in dejavu does not support math text

# Jan 29
_attending_: [efiring](@QWhXj01mSwmTjk5kN1H_qQ) @ksunden @QuLogic @tacaswell 

## Agenda
- [x] RSE updates
- [x] font discussions

## Notes
All PR review


# Jan 22

_attending_: [efiring](@QWhXj01mSwmTjk5kN1H_qQ), @melissawm, [@anntzer](@pXw4hSgTQF2--OciPYwa1w), @story645, @ksunden, @tacaswell, @scottshambaugh, @timhoffm , @QuLogic 

## Agenda
- [x] RSE updates
- [x] NASA updates
- [ ] 3.11 status

## Notes 

### RSE updates
- Tom:
    - minimal work, in operation/project
- Melissa: Created a doc for discussion around triage team: https://hackmd.io/@matplotlib/r1g8K31Ubx
    - [ ] Melissa to create a subcategory on discourse for maintainers to add/nominate people to the triage team
    - [ ] Melissa to figure out a way to add AI use disclosure/information on docs
    - [ ] Caswell will investigate GH group permissions / external contributor for triage
- Kyle:
    - still waiting on contract
    - mostly review/issue

### NASA
- slow progress
- final report for previous roses is due in April

### 3.11
- [#30059 drop intermediate buffer](https://github.com/matplotlib/matplotlib/pull/30059)
    - blockers: 
        - design decision is wrong, properly would be to have intermediate buffer in different position 
        - slight issue around positioning fraction bars when drawing math
            - want to draw fraction bars exactly on pixel, requires controlling snapping better 
                - accept snapping b/c improvement over fuzzyness
                - bars are slightly too low/high/wrong position - fix is figure out if floor or ciel rounding
                - bar positioning issue is independent of buffer 
            - is here to avoid regenerating all the fraction images
                - maybe kick fraction image regenerating down the road
        - ok w/ edge case of overlapping glyphys? 
            - yes
        - consensus: should go in, put buffer positioning and fraction bar on "nice to have" stack

- [#30974 widget blitting](https://github.com/matplotlib/matplotlib/pull/30974)
    - not sure if problen is in MNE tests, widget blitting code, or base canvas API (vs Gui canvas API) 
        - fire events where handler forces a draw that asks for a renderer that the base canvas doesn't have
        - MNE is holding a canvas reference that calls for a non-existent canvas

## other PRs
- [#30974 right click context menu](https://github.com/matplotlib/matplotlib/pull/30976) 
    - turn off able b/c other tools provide context menu
        - general API figure.add_context_menu + callback
    - squeeze into toolbar? 
        - add hamburger to toolbar w/ additional tools likes context menu
 -[#30980 log axes on 3d plot](https://github.com/matplotlib/matplotlib/pull/30980)
    - needs reviews, would fix oldest open bug!
    
    
# Jan 15
_attending_: [efiring](@QWhXj01mSwmTjk5kN1H_qQ), @ksunden, @QuLogic, @melissawm, @story645, @ayshih, @timhoffm 

## Agenda
- [x] RSE updates
- [x] NASA updates
- [x] 3.11 status
- [x] review Albert's PRs
    - [x] [Accuracy bugs with image resampling ](https://github.com/matplotlib/matplotlib/pull/30184) - sig changes post review
- [ ] [name=timhoffm]review [blitting errors in {check, radio} button widgets](https://github.com/matplotlib/matplotlib/pull/30945)

## Notes
### RSE updates
- Melissa
    - getting re-onboarded
    - discovering build issues
    - thinking about triage team and how to get recruitment going
- Elliott
    - writing statement of work
    - waiting on responses from @tacaswell to start contract process
    - alt-text is almost done, but needs some finishing touches
- Kyle
    - still waiting on contract
    - little bit of issue review
    - setting up hi-dpi monitor
- Tom
    - little mpl work, swamped with other things

### NASA
- contracts are moving 

### 3.11
- still holding on Antony's PR
    > https://github.com/matplotlib/matplotlib/pull/30059?    
    - need to check one last thing and merge
    - need to check do a scan thourgh one final time to make sure that nothing changes by too much
- https://github.com/matplotlib/matplotlib/pull/30945
- 
### image resampling
- grid lines and pixel lines not lining up w/ non-affine transforms
- this PR loosens tolerances to avoid updating baseline images, gets resolved by font prs 
    - text changes b/c of change in computation of kernal used in text rotation
    - 20 images had to be changed, about 40-45 loosened for text & noted with TODO
- [30824](https://github.com/matplotlib/matplotlib/pull/30824) b/c bivariate was using agg interpolator for non-viz purposes, agg takes shortcuts

### radio/check buttons
- merged 
- work left in whats new & todos: not all widgets work properly after swapping canvas
    - blitting should be better encapsulated, hindered by how state is stored in widgets
        - store if user wants blitting and if canvas supports blitting 
    - use case is standalone figure that might get attached to canvas

# Jan 8
_attending_: [@efiring](@QWhXj01mSwmTjk5kN1H_qQ), @tacaswell, @QuLogic, @ksunden, @timhoffm, @story645 

## Agenda
- [ ] RSE updates
- [x] NASA updates
- [x] 3.11 status
- [x] 3.10.8 / build overhaul status - RELEASED
- [x] [name=@rcomer] Trial [Discourse Chat](https://meta.discourse.org/t/discourse-chat/230881) as replacement for Gitter?
- [x] [name=@hannah] GSOC: backend API improvements
    - builds on [versioning](https://github.com/matplotlib/matplotlib/pull/30777)
    - [GraphicsContext data classes](https://github.com/matplotlib/matplotlib/pull/30811)
    - [fonts](https://github.com/matplotlib/matplotlib/issues/30890#issuecomment-3690830981)
- [x]  Docs are getting big on digital ocean 

## Notes
### RSE updates
* Melissa
    - starting this week!
* Tom
    - very busy, some grant management
* Kyle
    - Purchased some ARM machines with money from pevious grant
    - linux on ARM is harder than we expected
* Elliott
    - not much over break
    - review a few things, update freetype and harfbuzz
        - few minor changes that are improvements

### NASA updates
- Starting to spend money on ROSES 2024
    - Y2 funds are in-process
- need to write grant report on ROSES 2020

### 3.11 status
- still need to review Antony's PR
- image resampling PR affects some text images
    - one in, one pending
- widget canvas handeling PR was not enough
- aim for RC end of next week
- Elliott is release manager
- https://github.com/matplotlib/matplotlib/pull/30777 (reviewed and merged)
- https://github.com/matplotlib/matplotlib/pull/30871/changes (reviewed)
- https://github.com/matplotlib/matplotlib/pull/30886 (reviewed and merged)

### chat in discourse?
- no love of element/gitter expressed
- proposal:
    - turn discourse chat on
    - redirect conversation from gitter -> discourse for a month
        - posts made and pinned on matplotlib/community/incubator
    - at end of month either turn it off or document and shutter element channels
- Turned it on and created 3 channels
    - @rcomer should weigh in on how to further organize

### 3.10.8

- out and merged up
- publish removed from the main repo
- need to double check that the trusted publisher from the main repo removed on pypi side
- publishing from external repo worked

### docs too big
- checked out docs are now 32G+
- running out of disk space on venus (our file server)
- git seems to be doing a very good job at compression (the `.git` folder is 6-7G)
- to get out of the jam we will prune old micro docs for non-current releases and replace with permenant redirects in caddy.
    - can get back if we _really_ need it
    - will buy us some more time before we run out of disk again
```
163M    1.2.1
196M    1.3.0
173M    1.3.1
249M    1.4.0
249M    1.4.1
249M    1.4.2
189M    1.4.3
230M    1.5.0
236M    1.5.1
233M    1.5.3
205M    2.0.0
203M    2.0.1
204M    2.0.2
134M    2.1.0
126M    2.1.1
143M    2.1.2
146M    2.2.0
174M    2.2.2
169M    2.2.3
168M    2.2.4
173M    2.2.5
183M    3.0.0
152M    3.0.2
172M    3.0.3
169M    3.1.0
200M    3.1.1
191M    3.1.3
194M    3.2.0
201M    3.2.1
199M    3.2.2
285M    3.3.0
288M    3.3.1
285M    3.3.2
290M    3.3.3
298M    3.3.4
300M    3.4.0
301M    3.4.1
301M    3.4.2
301M    3.4.3
579M    3.5.0
628M    3.5.1
627M    3.5.2
628M    3.5.3
606M    3.6.0
606M    3.6.1
588M    3.6.2
589M    3.6.3
626M    3.7.0
631M    3.7.1
629M    3.7.2
629M    3.7.3
573M    3.7.4
629M    3.7.5
658M    3.8.0
659M    3.8.1
659M    3.8.2
662M    3.8.3
662M    3.8.4
594M    3.9.0
595M    3.9.1
602M    3.9.2
555M    3.9.3
571M    3.10.0
572M    3.10.1
572M    3.10.3
572M    3.10.5
573M    3.10.6
573M    3.10.7
573M    3.10.8
```
- Dropping 1.x and 2.x will save 2.7G
- Dropping 3.0.x is 334M
- Dropping 3.1.x is 368M
- Dropping 3.2.x is 395M
- Dropping 3.3.x is 1.2G
- Dropping 3.4.x is 901M
- Dropping 3.5.x is 1.8G
- Dropping 3.6.x is 1.8G
- Dropping 3.7.x is 3.1G
- Dropping 3.8.x is 2.6G
- Dropping 3.9.x is 1.8G
- Dropping 3.10.x is 3.4G

### GSOC backend project
- hard part is the design phase - how 
    - moving backend function signatures from parameter list to data class of backend parameters
        - in fonts, all the new feautures only available indirectly
            - drawing text as last parameter takes text object
            - measurement doesn't take text object so can't compute directly
    - is likely a medium sized GSOC project, w/ a lot of testing work 
    - @tacaswell has some concerns about this not having enough concrete upside for the cost of the code churn
- alternative idea
    - PR 30516 / issue [30515](https://github.com/matplotlib/matplotlib/issues/30515)
    - how to push more "native" overlays into the backends to allow cross hairs and similar
    - try out new scheme for passing things into the backend using dataclasses as entry point to using the pattern in the backend
