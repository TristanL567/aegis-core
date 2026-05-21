relevant-when: Open this drawer when UI changes after load and users need perceivable status or context changes.

# Dynamic Content And Announcements

- Loading, saving, error, success, filtering, sorting, and route-change states
  may need status text or live region announcements when the change is not
  otherwise perceivable.
- Use polite announcements for routine status changes and assertive
  announcements only for urgent interruptions.
- Route changes in single-page applications should update page title, main
  heading, and focus context where needed.
- Dialogs and modals should communicate their label, modal state, initial focus
  target, and relationship to the background content.
- Toasts should not be the only place important information appears, especially
  when they auto-dismiss.
- Skeletons, spinners, and optimistic updates need accessible status or fallback
  text when they affect task completion.
