# Architecture Overview

## Components

- HabitManager: add/remove/list habits
- ReminderService: send notifications
- Analytics: generate reports

## Diagram

[User] → [UI] → [HabitManager] → [Data]
                      ↓
              [ReminderService]
