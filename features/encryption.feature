Feature: Encryption

    Scenario: encrypt/decrypt journal
        Given application
        And journal with random content
        And random password
        When encrypt journal
        Then content of journal is not identical to initial content
        When decrypt journal
        Then content of journal is identical to initial content
