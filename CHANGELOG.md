# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2022-07-11

### Added 

- Changelog file
- Pagination options to get modules
- Pagination options to get contents
- Pagination options to get contents by user
- Pagination options to get projects by user

### Changed

- API base URL moved to simply /api
- Create body of contents:
    - selectedLayer to selected_layer
    - Customer to customer
- Create body of customer:
    - Name to name
    - NIF to nif
    - Login to username
    - Password to password
    - Email to email
    - UserLevel is not necessary anymore
- Update body of customer has the same changes of creating a customer
- Create body of project:
    - Contents to contents
- Route to login moved to /auth/token
- Route to register customer moved to /customers/add
- Route to create a new Module requires an admin level
- Route to get project info by user moved to /projects/get/user/{id}

### Fixed

- Fixed passwords with hash in database