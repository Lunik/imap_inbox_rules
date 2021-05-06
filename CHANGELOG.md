# CHANGELOG

## v0.3.0

### Enhancements:
- N/A

### Bug fixes:
- [GitHub Action] Fix workflow preventing merge commit
- [GitHub Action] Enable CI when push on `master`

### Documentation:
- N/A

## v0.2.0

### Enhancements:
- [Coverage] Replace CodeCov with SonarCloud
- [SonarCloud] Add QA scan
- [SonarCloud] Add coverage
- [SonarCloud] Add vulnerability scan
- [SonarCloud] Add quality gate
- [SonarCloud] Improve code smell
- [GitHub action] Disable some pipeline if there are no code modification

### Bug fixes:
- [CodeQL] Add autobuild step

### Documentation:
- [SonarCloud] Add badges
- [CodeCov] Remove all references to the tool

## v0.1.0

### Enhancements:
- [GitHub Action] Add badges in README.md (#5)
- [GitHub Action] Disable commit count when merging on master (#6)
- [GitHub Action] Block merge on master if there are "Merge commit" present (#9)
- [CI] Add & run Lightweight IMAP server for tests (#4)
- [CI] Add init script for setup lightweight IMAP server (#4)
- [Exceptions] Rename `connector.ConnectorNotFoundException` into `connector.ConnectorNotFound` (#4)
- [Exceptions] Create new exception `connector.ObjectWithoutConnector` when an object is initiated without connector and a method requiring it is called (#4)
- [Exception] Create new exception `mailbox.MailboxNotFound` when selecting inexistant mailbox (#4)
- [Exception] Create new exception `mailbox.MailboxCheckFailed` when mailbox check fail (#4)
- [Exception] Remove exception `model.imap.ImapMailboxWithoutConnector` replaced by `connector.ObjectWithoutConnector` (#4)
- [Exception] Create new exception `model.imap.ImapMailNotFound` when mail os not found (#4)
- [Exception] Create new exception `model.imap.ImapMailNotLoaded` when mail is not loaded and a method requiring it is called (#4)
- [ImapConnector] Allow to create connection with SSL-less security (#4)
- [ImapConnector] Allow to select mailbox with method `ImapConnector.select_mailbox` (#4)
- [ImapConnector] Allow to search for mail with method `ImapConnector.search_mail` (#4)
- [ImapConnector] Allow to fetch mail with method `ImapConnector.fetch_mail` (#4)
- [ImapMail] Create class to represent Mail object (#4)
- [ImapMail] Allow to decode mail header and body (#4)
- [ImapMailbox] Store mailbox full path in attribute `ImapMailbox.full_path` (#4)
- [ImapMailbox] Use `ImapMailbox.full_path` attribute in `ImapMailbox.list_mailbox` method (#4)
- [ImapMailbox] Create `ImapMailbox.select` method to select the current mailbox (#4)
- [ImapMailbox] Add `ImapMailbox.count_mail` property to list email in mailbox (#4)
- [ImapMailbox] Allow to search for mail with method `ImapConnector.search_mail` (#4)

### Bug fixes:
- [ImapMailbox] Fix regex in `from_bytes` method when mailbox as no attributes (#4)

### Documentation:
- Move documentation in [it's own directory](documentation/) (#7)
- [LICENSE] Add GPL3 license (#8)
- [Codecov] Update link to Codecov in README.md (#10)

## v0.0.1

Pull Request #1

### Enhancements:
- Initialise project
- [IMAP Connector] Creation
- [IMAP Connector] Allow to authenticate to IMAP servers
- [IMAP Connector] Allow to list mailboxes
- [IMAP Connector] Allow to list sub-mailboxes
- [PyTest] Add unitest
- [CodeCov] Add coverage checks
- [PyLint] Add lint tests
- [CodeQL] Add vulnerability check

### Bug fixes:
- N/A

### Documentation:
- Create [CHANGELOG](CHANGELOG.md)
- [IMAP Connector] Add exemples on [README](README.md)
