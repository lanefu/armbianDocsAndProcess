# Armbian Issue Management #

## Overview ##
TLDR; Keep task discussions in the forum.

Tasks associated with code will have an issue created in GitHub, but **all dialog regarding task will reside on the forum** in a thread containing the github Issue ID of the task.


## Task Creation Procedure ##

1. Create issue in [Armbian GitHub Repo](https://github.com/igorpecovnik/lib/issues) under appropriate milestone
1. Copy the numeric ID of issue created
1. Create new thread under the Tasks Topic on the [Armbian Forums](http://forum.armbian.com/index.php/forum/14-tasks/)
    - Use the the naming convention of `[ISSUE_ID] - Issue Name`
1. Copy the URL of task forum thread just created
1. Create comment on GitHub Issue with the following Content:

```
Please keep all discussion for this issue on the forum thread available below:

[URL](URL)

```

## GitHub Issues ##

GitHub Issues provide an easy method to track and filter tasks by using tags and milestones.  Issues also make it easy to easily associate commits and merge requests with a task.  

### Labels ###

Use labels identify the purpose of a task.

#### bug ####

`bug` is used to tag tasks that address Armbian-level bugs

#### not-our-bug ####

`not-our-bug` is used to identify tasks that are bugs in upstream code.  They are not Armbian bugs, but may impact Armbian.

#### enhancement ####

`enhancement` is used to identify tasks that are new features for Armbian.

### Milestones ###

Use milestones to divide tasks into claimed and unclaimed work.

#### Claimed ####

Tasks which have an owner can be filed under the `claimed tasks` milestone

#### Unclaimed ####

Tasks which need an owner should be assigned to the `unclaimed tasks` milestone.

## Forum Tasks ##

Sometimes support discussions can become tasks.   A forum admin can assist in moving the thread to Tasks forum group.  A cooresponding issue will need to be created.

## Future Process Improvements ##

Enhancements desired for this process \(This should be a task!\)

### Issue Hook ###

Ideally we can have a forum thread created upon issue creation.  This will same some time.
