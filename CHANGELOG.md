# CHANGELOG

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
- [CI] Add & run Lightweight IMAP server for tests
- [CI] Add init script for setup lightweight IMAP server
- [Exceptions] Rename `connector.ConnectorNotFoundException` into `connector.ConnectorNotFound`
- [Exceptions] Create new exception `connector.ObjectWithoutConnector` when an object is initiated without connector and a method requiring it is called
- [Exception] Create new exception `mailbox.MailboxNotFound` when selecting inexistant mailbox
- [Exception] Create new exception `mailbox.MailboxCheckFailed` when mailbox check fail
- [Exception] Remove exception `model.imap.ImapMailboxWithoutConnector` replaced by `connector.ObjectWithoutConnector`
- [Exception] Create new exception `model.imap.ImapMailNotFound` when mail os not found
- [Exception] Create new exception `model.imap.ImapMailNotLoaded` when mail is not loaded and a method requiring it is called
- [ImapConnector] Allow to create connection with SSL-less security
- [ImapConnector] Allow to select mailbox with method `ImapConnector.select_mailbox`
- [ImapConnector] Allow to search for mail with method `ImapConnector.search_mail`
- [ImapConnector] Allow to fetch mail with method `ImapConnector.fetch_mail`
- [ImapMail] Create class to represent Mail object
- [ImapMail] Allow to decode mail header and body
- [ImapMailbox] Store mailbox full path in attribute `ImapMailbox.full_path`
- [ImapMailbox] Use `ImapMailbox.full_path` attribute in `ImapMailbox.list_mailbox` method
- [ImapMailbox] Create `ImapMailbox.select` method to select the current mailbox
- [ImapMailbox] Add `ImapMailbox.count_mail` property to list email in mailbox
- [ImapMailbox] Allow to search for mail with method `ImapConnector.search_mail`

### Bug fixes:
- [ImapMailbox] Fix regex in `from_bytes` method when mailbox as no attributes

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
