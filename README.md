# Python Learning and Review 2026

This repository is used to practice, review, and explore python topics for personal learning and growth, as well as to document progress and insights gained throughout the journey.

## Goals
- Strengthen understanding of core Python concepts.
- Explore advanced Python topics and libraries.
- Build projects to apply learned concepts.
- Maintain a record of learning progress and key takeaways.

## branching strategy

Because this repository is for personal learning and review, the branching strategy is kept simple to facilitate experimentation and progress tracking, but I do want to maintain a clear distinction between stable and development work.

From this point forward, all development work will be done in the `develop` branch and merged into the `main` branch only when it is demonstrated to be stable.

- `main` branch: Contains the stable version of the project.
- `develop` branch: Used for ongoing development and integration of new features.

### Feature Branches
The use of feature branches is optional because this is a personal repository with one contributor, but any feature branches should be created from the `develop` branch and squash merged back into `develop` when complete.

- `feature/<feature-name>`: Naming convention for feature branches, where `<feature-name>` describes the feature being developed.
- `optimization/<optimization-name>`: Naming convention for optimization branches, where `<optimization-name>` describes the performance improvements being made. This should only be used for changes that improve performance without altering functionality.
- `refactor/<refactor-name>`: Naming convention for refactor branches, where `<refactor-name>` describes the code refactoring being performed. This should only be used for true refactoring tasks, not for optimization or anything that adds functional changes to the code.
- `bugfix/<bugfix-name>`: Naming convention for bugfix branches, where `<bugfix-name>` describes the bug being fixed.
- `documentation/<documentation-change-name>`: Naming convention for documentation branches, where `<documentation-name>` describes the documentation being added or updated. This should only be used for purely documentation-related changes.
- `workflow/<workflow-change-name>`: Naming convention for documentation branches, where `<documentation-name>` describes the documentation being added or updated. This should only be used for purely documentation-related changes.
