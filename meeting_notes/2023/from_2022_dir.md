
# 2 March 2023

_attending_:

## Agenda

### Old business

### New business
- [x] RSE reports
- [x] 3.7.1 release?
- [x] Stale label? 
- [x] 3.8 goals? 
- [x] pydata-sphinx-theme 0.13 issue
- [x] Matplotlib website has 2 references of 3.6 being stable (matplotlib.org announcements, https://matplotlib.org/stable/index.html)

### Issues and PRs

- [x] [name=QuLogic] [#2123](https://github.com/matplotlib/matplotlib/issues/2123), [#13648](https://github.com/matplotlib/matplotlib/issues/13648), and [#19955](https://github.com/matplotlib/matplotlib/issues/19955) are semi-duplicates, but they've all got some long conversation on them, so I'm not sure which should be closed

## Notes

### RSE reports
- @tacaswell: PR review
- @ksunden: typing PR, close to merged/reviewed; PR review; scipy tutorial proposal
- @QuLogic: PR review, issue triage, 3.7.1 close, checked all dependencies in Fedora for issues with 3.7.0

### 3.7.1
- ready to go basically (main is pandas incompatibility)
- [results of Fedora dependency checks](https://src.fedoraproject.org/rpms/python-matplotlib/pull-request/37#comment-132230); appears to be no major issues to fix for 3.7.1
- tag tomorrow?  @QuLogic and @ksunden
- QHull license issue

### Stale bot

- only doing 5-10 per day
    - this is due to a limit we set, could turn up
    - the current rep-rate seems good
- be more cautious about adding "keep" label 
    - just interacting with it is enough to get 365 days of life
    - useful to let these things be re-circulated

### pydata-sphinx-theme 0.13

- in 0.13.0 pst changed how they handled the logos
- this broke how we updated the logos in mpl-sphinx-theme
- @jklymak has a PR in with pst to enable what we need
- mst will also have to change which will make specifying the logo simpler
- this will require changes to most of our packages
- hard-pin mpl-sphinx-theme and mpl-sphinx-theme
    - yes, we do want to do this

### axis limits offer autolimming
- [#2123](https://github.com/matplotlib/matplotlib/issues/2123), [#13648](https://github.com/matplotlib/matplotlib/issues/13648), and [#19955](https://github.com/matplotlib/matplotlib/issues/19955)
- don't have api for asking artist its limits on a given sub-range
    - how can we efficiently do that?
    - can do in pandas or xarray, but hard for arbitraty paths
- close just one of them? 
- need to go through the transform stacks?  
- could add an API for ylim given xlim to each Artist
    - should be done as part of bigger data pipeline redesign

### 3.8 longer term plans...
- Medium scale projects for RSEs one motivator
- @QuLogic: 
    - hiDPI later in stack to be more flexible between displays
    - contours overlap with alpha anti aliasing artifacts
        - Agg code exists to try and fix this
- @ksunden
    - typing work
    - unit support documentation?
- @tacaswell 
    - multiple versions of freetype image comparisons
        - test versus previous dev
        - on releases as separate wheel
    - TTC fonts
        - more than one font (C layer threading)
        - doable: just need to be able to unpack; need a syntax to get the correct font (tuple or string with suffix)
- other
    - Transform objects
        - track what co-ordinate systems they go between
        - move to C to gain speed? Numpy slow for small arrays
            - pybind11 might make this easier
        - open GL libraries for matrix math that may do this for us
        - weak references between parents and children make hard to move to C
    - legends overhaul?
        - handler on Artists to make artist for the legend.  Then decoupled from Artist.
        - add Artist API to have "get_legend" allows pushing updates. 
        - or sync properties...
            - composite Artists
    - overhaul rcParams:
        - dict subclass
        - custom object that has mapping API
        - https://github.com/matplotlib/matplotlib/issues/24585


----------------------------

# February 23, 2023
_attending_: ksunden, chahak13, hannah, ianhi, efiring, jklymak, tacaswell, QuLogic, scottshambaugh, greglucas, anntzer

## Agenda

### Old business

### New business
- [x] RSE reports
- [x] PRs 329; draft:false 47
- [x] ipympl dicussion
- [x] 3.7.1 critical bugs?
- [ ] 3.8 goals? 

### Issues and PRs
- [ ] [name=jklymak] [name=anntzer] https://github.com/matplotlib/matplotlib/pull/17497 - how new C++ can we use?
- [ ] [name=chahak13] https://github.com/matplotlib/matplotlib/pull/25259 - `markersize` in scatter
- [x] [name=efiring] https://github.com/matplotlib/ipympl/issues/497 - ipympl design questions
- [x] [name=scottshambaugh] https://github.com/matplotlib/matplotlib/pull/23485 - 3D hover coordinates
- [x] [name=scottshambaugh] https://github.com/matplotlib/matplotlib/pull/25272 - 3D exact axis limits - deprecate or no?

## Notes

### RSE reports
- Caswell: SDG for 100h to do scraping arXiv
- Kyle: 3.7 wrap up; Release procedure docs.  Accepted for GSoC so organizing that.  Proposal for SciPy.
- QuLogic: catching up

### ipympl
 - Python is being taught in jlab more and more
 - "nbagg" is backend for "classic" backend that we ship and behaves very much like the other GUI toolkits
     - saves when you save
     - can close the windows
     - does not work in jlab (for very good security reasons)
 - ipympl is the replacement
     - but has had some missing features (e.g. not saving when you exit which is now fixed)
 - has some concerning design choices
     - floating / popup toolbar
     - no close button to "turn off"
 - still needs some work
     - do we have enough user feedback?
     - how to we get the usability issues addressed?
 - how is ipympl goverened?
     - adhoc
     - sometimes self-merge due to lack of people who can review
 - how do we teach jupyter users to use ipympl rather than inline?!
 - ipympl seems to break often
     - ipympl has been moving slow
     - ipywidgets, jupyterlab, and matplotlib all break ipympl upstream
 - if we want to make this the default backend on jlab we need more something
 - there are some automated tests (galatta) that do run
 - possible things to do:
    - ping mpl devs on PRs
    - do we need to find money for this?
- installation problems
    - split js / Python can be painful?
    - this is due to how ipywidgets installs work
- some issues are due to details of how ipywidgets works
    - e.g. blocking 
- how do we push upstream to fix things?
- Elliott has a PR to use playwright to test webagg
    - should be adaptable
- steps going forward
    - better governance
    - some part time paid support
    - bot to make issues when tests fail
    - mpl needs to stop breaking ipympl
        - need a ipympl UAT

### 3.7.1 critical bugs?
- units + pandas
    - reverted the fix and re-opened the original issue
- missing license file
    - not clear why this is a new problem
    - pragmatic solution is to add a `wget` step to the jobs to pull the license file pre-emptively
- aim for 3.7.1 end of next week

### markersize for scatter
- have a draft PR
    - touches path collections and 3D path collections
    - https://github.com/matplotlib/matplotlib/pull/25259
- tests pass locally, but fail on CI
- please take a look to make sure this is a good path before adding tests
- suggestion: write the whats new

### 3-D hover co-ordinates
- no way to snap to data
    - snap to nearest plane?
    - or remove?

### 3D Padding
- axis limits have padding even if set automatically
- break custom limits tests
- rcParam?
- make consistent w/ margins for 2D axes?

-------------------------
# February 16, 2023
_attending_:
## Agenda

### Old business


### New business
- [x] RSE reports
- [x] PRs 319; draft:false 40

### PRs and Issues
- [ ] [name=jklymak] [name=anntzer] https://github.com/matplotlib/matplotlib/pull/17497 - how new C++ can we use?
- [x] [name=jklymak] Stale bot? https://github.com/matplotlib/matplotlib/pull/25163
- [x] [name=jklymak] Reorg galleries [#25209](https://github.com/matplotlib/matplotlib/pull/25209)
    - galleries/gallery, galleries/tutorials, galleries/plot_types
    - See https://github.com/matplotlib/matplotlib/pull/25218 for motivation (mixed rst and py = sphinx-gallery docs)
- [x] [name=jklymak] [Theta transforms in polar removal](https://github.com/matplotlib/matplotlib/pull/24834)
    - is this idiomatic? Seems bad to have a flag in all the examples?


## Notes

### RSE reports
- @ksunden; 3 .7 release!!! yay
- pandas issue: check for covnerter and units 
    - confuses their converter
    - strings w/o units resets the converter to Categorical
    - "UTC" default unit? versus `None`
- @tacaswell: also 3.7 release...
   
### PR s and Issues

####  C++ compiler? https://github.com/matplotlib/matplotlib/pull/17497
- C++ 17 should work. Why old C++?
- manylinux wheels container? and MS compiler?
- advantages? 17 versus 11?

#### Stale bot
- worth trying?

#### reorg galleries
- `galleries/examples`, `galleries/tutorials` etc instead of /examples, /tutorials
- website configuration stored in https://github.com/matplotlib/matplotlib.org
    - would have to add the re-write rules to give redirects from /gallarly -> /examples

#### colormap tuple
- `(color, alpha)` seems general agreement that its fine

#### State of ipympl?
- usability issues? 
- 



-----------------
# February 9, 2023
_attending_:
## Agenda

### Old business

### New business
- [x] RSE reports
- [x] PRs: 316, draft:false 36 
- [x] [name=hannah] [scipy tutorial: feb 22](https://www.scipy2023.scipy.org/present)
    - [Link to example submissions by scipy conf](https://github.com/scipy-conference/scipy-conference/tree/master/data/tutorial_submissions) 
- [x] 3.7.0 final tomorrow?
- [x] [name=Melissa] Update: GSoD proposal
    - Deadline for orgs is March 24, we are working on it. Suggestions welcome! [link to proposal](https://hackmd.io/@matplotlib/gsod2023)
- [x] SDG to extend the arxiv scraping work

### Issues and PRs
- [ ] [name=hannah] [#24691: (color, alpha) color spec](https://github.com/matplotlib/matplotlib/pull/24691#issuecomment-1419756150)
- [x] [name=jklymak] [Stale bot](https://github.com/matplotlib/matplotlib/pull/25163)
    - [will it even work](https://github.com/actions/stale/issues/792)?  Stagger start/stop dates over time? 
    - offline tools to do old issues/PRs first?
- [x] [name=jklymak] [pcolormesh deprecation dance, #25162](https://github.com/matplotlib/matplotlib/issues/25162)
    - pcolormesh now stores internally as 2-D (versus flattening), but that breaks folks who were working around the flattening of retrned objects (data, facecolor etc)
- [x] [name=chahak13] ["size" argument in Collections](https://github.com/matplotlib/matplotlib/issues/1101)
    - Disclaimer: Really old issue
    - Is this still relevant? There seemed to be agreement that something had to change but doesn't show any update then. There is still no support for a `markersize` or equivalent.

## Notes

### RSE reports
- @tacaswell main job very busy
- @ksdunden: PR review; 3.7 release; ruff config in; data prototype work getting started.
- @melissawm New contributor meeting (w @ksunden).  Meeting with Teresa and Camron Riddel;
    - GSOD: deadline to 24 Mar (open 15 Feb) 
    - comment on proposal....
    - <https://hackmd.io/@matplotlib/gsod2023>

### Scipy23 tutorial:
- Feb deadline, July
    - Tutorials: July 10-11  |  Conference: July 12-14  |  Sprints: July 15-16
- Melissa, Kyle may go
- 2d tutorials, 3d conference, 2d sprints
- tutorials typically beginner side
    - 1/3 - 1/2 new attendees
    - recorded and on-line
    - maybe some focus on modern improvements
    - how to do things (compared to other paradigms?)
- Let's brainstorm here: https://hackmd.io/@matplotlib/scipy2023tutorial/edit

### 3.7.0 tomorrow(??)
- hopefully!
- try to do w/o Elliott
- backport 88 character limit to 3.7
- make sure highlights get to @story645

### GSOD
- currate examples
- sphinx-tag extransion directive
- vocabulary of tags?
    - learning paths...

### scrape archive for watermark
- SDG to do more of this $5k 100 h labour, + credits
- script that we can update...
- categorize by field.
- broader impact beyond Matplotlib

### markerize argument in Collections
- ["size" argument in Collections](https://github.com/matplotlib/matplotlib/issues/1101)
- `scatter(s=)`
- `markersize` or `size` has more semantic meaning, but still vectors
    - `s` Area based versus via diameter (line/plot uses diameter)
    - sometimes scaled by area of shape relative to circle (that in `Collections`).
    - `s` deprecation warnings is super disruptive
    
### Stale bot
- API limit
    - maybe new
    - wait an hour if you exceed limit
    - REST API limits
    - First time contributors need to get through new API
- Maybe explore offline

### pcolormesh getter
- need to add kwarg to getters...
    - old seaborn with new Matplotlib will be annoyed
    - flatten=True default, btu allow flatten=False
    - public properties?  


--------------
# February 2 2023

## Agenda

### Old business

### New business

- [x] RSE reports
- [x] PRs 325, draft:false 52, (40-odd actionable)
    - [name=@rcomer] mark inactive PRs and issues automatically?  
- [x] [name=Melissa] New contributor meeting next week (Feb 7)
    - Could we have a (tiny) live PR?

### Issues and PRs
- [x] [name=@anntzer] ECDF @tacaswell [#24728](https://github.com/matplotlib/matplotlib/pull/24728)
- [ ] [name=@greglucas] Collections vs Containers and inheritance vs composition [#25027](https://github.com/matplotlib/matplotlib/pull/25027), [#25128](https://github.com/matplotlib/matplotlib/issues/25128), [#24388](https://github.com/matplotlib/matplotlib/pull/24388)
- [ ] [name=@hannah] [color validation](https://github.com/matplotlib/matplotlib/pull/25025#issuecomment-1410845470)

## Notes

### RSE reports
 - Caswell: 3.7 work, starting to troll issue
 - Sunden: 
     - 3.7 work
     - tooling investigation
     - will pivot back to data-protoype next week
 - Melissa
     - GSOD project: if you have more feedback please add to hackmd, still have 10 days before it is due
    - https://hackmd.io/xRmN9nAPQUqU_-pm9dNekQ


### tooling
 - ruff
     - young, but used by other big (numpy, scipy, pandas) projects
     - linter written in rust (!)
     - very (very) fast, will include auto fixing + linting eventually
     - may looking to CI, but may not be worth the effort (linting is our fastest CI check)
     - may add a config so devs can use it


### New Contrib meeting
- anyone come to do live PR?
    - maybe regularly?

### automatic stale / close PRs

- what do we want to automate about PRs
    - reminders / ping
    - add orphan tag?
- frequently we are the ~~problem~~ bottle neck on the review
- closing PRs might be too agressive
- we will try a bot
    - Melissa will "copy" responses and come up with a draft bot.
    - A few points the bot could take care of:
        - Move inactive PR to draft
        - Attach a "needs attention" label
        - Mark PR as "orphan" if author is unresponsive
        - Investigate a "needs consensus" label
        - Stretch goal: pick 5 stalled issues for discussion for next meeting

### Issues 
- https://github.com/matplotlib/matplotlib/pull/25129 (3.7.0 blocker)
    - generalized concerns that the only way to extend `Cursor` is sub-class it.  Not how we would do it today, but grandfather it in and leave it alone.  Maybe re-consider later, but do not want to hold 3.7 over.
- https://github.com/matplotlib/matplotlib/pull/25126 (3.7.0 blocker)
- #24728 ECDF:
    - deal w/ NaN / masked by erroring, expecitng user to strip or fill as they need (slightly different stats in eitehr case)
- Collections vs Containers


-----------------
# January 26, 2023

## Agenda

### Old business

- [x] GSoD?  Any mentors?
    - Working with Sphinx Gallery on rst/*.py integration: https://github.com/sphinx-gallery/sphinx-gallery/pull/1071
    - [Template/draft proposal](https://hackmd.io/@matplotlib/gsod2023) - feel free to add comments or edit


### New business
- [x] RSE reports
- [x] First time contributor project
    - while adding perhaps add labels, and consider moving stalled things to draft.


### Issues and PRs

- [ ] [name=jklymak] Replite console? https://github.com/matplotlib/matplotlib/pull/22634
- [x] [name=jklymak] spectral functions (again) https://github.com/matplotlib/matplotlib/pull/22828


## Notes

### RSE reports
- RSE: 3.7 largely
- Kyle: line length change in
- suggested list of projects into numfocus
- Melissa: 
    - existing PRs where help? 
        - add labels and move to draft if applicable (and comment so author knows)
    - GSOD...

### Google Summer of Docs
- 15 Feb
- @melissawm 
- Proposal to google: short.  https://hackmd.io/xRmN9nAPQUqU_-pm9dNekQ
- labels to example gallery? @melissawm  would be interested in (co-)mentoring 
- Feel free to edit or add comments.
- Other ideas for projects?  Need mentors to be responsible that milestones are met...
- Reporting: 
    - monthly short form
    - write case study at end
    - Example of final output: [NumPy Case Study from 2021](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2021:-NumPy-Case-Study)
- timeline flexible between May-Nov

### Sphinx gallery PR

- https://github.com/sphinx-gallery/sphinx-gallery/pull/1071

### mlab spectral...
- deprecate for 3.8
    - removal note should include exmplaination as to why our plots are wrong
    - direct to use scipy directly

### replite console
- interactive plots
- good for teaching tool
- 

-------------
# January 19, 2023
_attending_: @tacaswell @jklymak @oscargus @melissawm @story645 @ksunden @IGuKs80UTJCig4yt6Zos7w @QWhXj01mSwmTjk5kN1H_qQ @QuLogic 

## Agenda

### Old business

### New business
 
- [x] RSE reports
- [x] [name=oscargus] How to interpret min version (for NumPy)? https://github.com/matplotlib/matplotlib/pull/24992
   - MPL: All minor versions of numpy released in the 24 months prior to the project, and at minimum the last three minor versions.
   - NumPy: All minor versions of NumPy released in the prior 24 months from the anticipated release date with a minimum of 3 minor versions of NumPy
   - "All minor versions" referring to first or last release of a minor verion? 
   - In particular 1.21.0 was released June 22 2021, but 1.21.6 was released April 12, 2022 (1.22.0 Dec. 31 2021)
   - NumPy drops based on first release. https://numpy.org/neps/nep-0029-deprecation_policy.html
- [x] [name=Melissa] [GSoD](https://developers.google.com/season-of-docs/docs/timeline) -  Organization applications are due February 15, 2023 at 18:00 UTC
    - [Example of project ideas to submit (from NumPy 2021)](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2021-Project-Ideas)
    - [Case study (output of the project)](https://github.com/numpy/numpy/wiki/Google-Season-of-Docs-2021:-NumPy-Case-Study)

### Issues and PRs
- [x] [name=timhoffm, jklymak] [Restrict all import in pyplot](https://github.com/matplotlib/matplotlib/pull/12743)
- [x] [name=tacaswell] [Sphinx-gallery section separator](https://github.com/matplotlib/matplotlib/pull/25021)
- [ ] [name=jklymak] [Mechanism for combining narrative docs and tutorials](https://github.com/matplotlib/matplotlib/issues/24746#issuecomment-1396303356)
    - No need to discuss actual content, but a plan for how to fix the tutorial/users-docs dichotomy would be nice.

## Notes
-----------------

### RSE reports
- Monthly new contrib meeting. Next one 7 Feb
- @ksunden CF time bug.  NEP changes down ine.  Still not there in terms of usefulness
    - hard to check isinstances with inheritence
    - Numfocus GSOC sign up
        - Projects list being developped: mathetex issues, hatching improvements (register patterns), bivariant colormap, speech bubble types? 
        - Let Kyle know of possible projects
        - Discussion of how to communicate with mentee and co-ordinate project.
- @QuLogic 
    - 3.7 release work
    - widget styling PR #24838
    - away for a few weeks.
    - web related configs/issues should be able to be handled by Tom/Kyle
- @tacaswell 
    - review + 3.7 work

### NumPy version changes
- 24 months first release of numoy version not last release
- our next release June/July: if near a drop date to hold support a little longer...  Be conservative as possible within needing features..

### Google Seasons of Docs
- announced.  Org applications 15 Feb
- find a person to work with? Grant system...
- our experience was somewhat inefficient
- Numpy: tutorials with tech writer.  Both very familiar with numpy.  Second time got someone who ended up as document lead.
    - organization
    - fresh eyes
    - cataloguing and architecting docs
    - remove duplication metadata cross linking
    - need to be careful with scoping
 
 ### cell delineation for tutorials
 
-  `# %% ` instead of `############...`
-  No objections

### import restriction on *
- `from matplotlib pyplot import *` restricting
- at least needs an API note so people can adjust
- numpy allows submodules
- maybe _should_ import somethings and make available in `mattplotlib.figure` for instance?
- Lazy importing? Scipy has something like that.  
    - https://scientific-python.org/specs/spec-0001/
- `pyplot.cm.` will still work...
- 

----------

# January 12, 2023
_attending_: @tacaswell, @rcomer, @QWhXj01mSwmTjk5kN1H_qQ (efiring) @oscargus, @jklymak, @greglucas, @ksunden, @story645, @QuLogic

## Agenda

### Old business

### New business
 
- [ ] RSE reports
- [x] 3.6.3 out?
- [x] 3.7 progress
- [x] [name=oscargus] https://github.com/matplotlib/matplotlib/pull/24825 in 3.7 or 3.8 (and in general, when should we stop backporting?)
   - Long standing issue that would be nice to get in (I guess)
- [x] [name=hannah] [documenting addfont](https://github.com/matplotlib/matplotlib/pull/24866) 
- [x] [name=jklymak] [Quick doc build](https://github.com/matplotlib/matplotlib/pull/24907)
- [x] [name=jklymak] [cftime issue](https://github.com/matplotlib/matplotlib/issues/24951)
    - how to handle users trying to use Formatters for other converter types (eg trying to use Matplotlib Datetime converters on cftime-converted floats).
- [x] [name=greglucas] [pcolormesh extra keywords and mapping](https://github.com/matplotlib/matplotlib/issues/24854)
    - Should a 'k' linestyle with masked elements in an array only apply to the unmasked cells?


## Notes

### RSE reports
- @tacaswell 3.7 wrap up
- @ksunden 3.7 as well
    - sphinx issues
    - mypy issues still
- @QuLogic 
    - 3.6.3 tagged and released
    - working on 3.7 
- 3.7 Deprecation:
    - needs review
- Widget PR:
    - downstream libraries need this.
    - styling checks and radio. Still needs cleanup
    - https://github.com/matplotlib/matplotlib/pull/24838
- 3.6.3 tagged and released
    - 3.6.x closed. No more backporting there please

### PRs and Issues

- https://github.com/matplotlib/matplotlib/pull/24825 in 3.7 or 3.8 (and in general, when should we stop backporting?)
    - merge
    - maybe needs a slight bit of test modification
- Documenting [addfont]((https://github.com/matplotlib/matplotlib/pull/24866))
    - are users to use it or not?
    - needs to be at a higher level than just addfont docstring.
    - docstring should have a caveat in it.
    - Should be fully documented at top of font_manager module. 
- speed up docs builds
    - [Quick doc build](https://github.com/matplotlib/matplotlib/pull/24907)
- cftime
    - [cftime issue](https://github.com/matplotlib/matplotlib/issues/24951)
    - cftime is a tool xarray uses that allows for interesting calendars
    - user was using cftime converters (happens automatically)
    - were manually setting to use our locators / formatters which breaks because data -> float -> string which is giving wrong values
    - we have no way to tell at draw time that there is an incosistency
        - can we find a way?
        - we do know what converter is being used, but have historically not done any validation / checking
        - we have a couple of hooks where converters and formatters could check that they are consintent with each other
    - keeping track of origin + offset of dates
    - could we standardize on _always_ using datetime64?
    - [link to cf conventions](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/build/ch04s04.html)
    - our conveter / formatter machinery is too implicit
        - not always clear to users what is going on
    - Actions (for @ksunden )
        - ivestigate a lightweight method of warning about incompatible converters / formatters (short term)
        - medium term think about how this will be used in new unit work
        - medium term think about how we can use numpy's dtype + unit machinery to simplify
-  [pcolormesh extra keywords and mapping](https://github.com/matplotlib/matplotlib/issues/24854)
    -  masks on edgecolors
    -  edgecolors not the main point; mesh shows domain, 
    -  3.3 and before used to work...
    -  could make a mesh-drawing method...
        -  helper around line collections.
        -  or poly collections
            -  thats `pcolor`
    -  been broken for quite a while and current behaviour makes sense.


-----------------


# January 5, 2023
_attending_: @story645 @QWhXj01mSwmTjk5kN1H_qQ @rcomer @ksunden @tacaswell 

## Agenda

### Old business

### New business
 
- [x] RSE reports
- [x] report on circlci security breach
- [ ] 3.7 final decisions
    - branch today?
    - fonts on windows?  Either revert or fix https://github.com/matplotlib/matplotlib/pull/24655
    - bump numpy (should have done this a while ago): https://github.com/matplotlib/matplotlib/pull/24887/files
    - styling of radio / check buttons https://github.com/matplotlib/matplotlib/pull/24838
    - legend outside of axes https://github.com/matplotlib/matplotlib/pull/19743
    - (https://github.com/matplotlib/matplotlib/pull/24047 which reverted https://github.com/matplotlib/matplotlib/pull/22360 and https://github.com/matplotlib/matplotlib/pull/22361).  Caswell's understanding is that the regression is gone, 24011 was an attempt to fix that regression in a constructive way but seems to also have othre problem.  Can we remove the critical tag and re-milestone to 3.8?
- [ ] increase style line length to 115 (only if we have time)

## Notes

### CI Keys: 
- There was a security issue (not specified) at circle, they said to rotate keys
    - we have read-only deploy keys for public repos
    - have write-capable deploy keys for devdocs (from main repo) and mpl-sphinx-theme
    - all re-generated

### RSE reports
- kyle: nearing end of typing adventure.  Has CI working with mypy, typed pyplot
- Tom: took time off, working on clearing 3.7 review queue
- Elliott: widget work, circleCI fallout


### 3.7 final work
- when should we branch?
    - target 1600 tomorrow 23-1-6

### [fonts on Windows](https://github.com/matplotlib/matplotlib/pull/24655)
- conflict between how windows and linux handle finding fonts.  Windows expects files in registry, whereas linux just uses font files
- Does `findfont` need a registered name or will it find them from the paths?
- were finding deleted fonts rather than use Windows API
- can always specify a file path for a font
- actions:
    - go with windows registry only @tacaswell 
    - xfail the test @tacaswell 
        - defer questions of how to test this to later
        - do we want to change the registry as part of the test?
        - opt in to running locally?
        - flag to only run an CI + windows?
    - need a manual test that this works @story645 
        - download a new font
        - use windows way to install it
        - remove mpl's font cache
        - verify the new font can be found
    - add behavior change note @tacaswell 

### Bump numpy to 1.20
- currently get warnings 

### [styling of radio / check buttons]( https://github.com/matplotlib/matplotlib/pull/24838)
- scatter for buttons, and deprecated access to styling radio buttons, but downstream wants to style.
- discussion of list of dict vs dict of list

```
     label_props=[{'color': 'k'}, {'color': 'r'}, {'color': 'g'}],  # <- list of dicts
￼    frame_props={'edgecolor': ['k', 'r', 'g']},   # <- dict of lists
￼    check_props={'facecolor': ['k', 'r', 'g']},
```
- decisions
    - agree that consistent API of dict of list is esaier
    - agree to pass on broadcasting for now

### [legend outside of axes](https://github.com/matplotlib/matplotlib/pull/19743)
- needs second review

### [vertical space in latex](https://github.com/matplotlib/matplotlib/pull/24011) 
- Is this actually critical?  The issue it fixes was fixed by reverting two other PRs 

### Hatch with Pie
- needs second review

### https://github.com/matplotlib/matplotlib/pull/24085/files

### sha in footer of docs

https://github.com/matplotlib/mpl-sphinx-theme/pull/54/files

- do we want to put the date in as well?
    - eh
actions:
 - get as screen shot @tacaswell 
 - Jody says "just do it" with expidited review

### increase accepted style length
- currently <80 (so 79)
- options:
    - 88 (<89)
    - 115
- concern:
    - make sure the side-by-side view of diffs still work (2 wide on github)
    - be able to get at least 2 (maybe 3) panels up in a text editor
- action:
    - open PR adjusting it to 88 @tacaswell 
