Test your agent
===============

**Last checked:** |last_checked| against Agentplace's public documentation.

Use this guide before you publish, and again after every change to your knowledge or rules.

Steps
-----

1. Open a fresh session for each question. A long chat carries earlier answers into later ones and can change them.

2. Record the model, the date and the question before you read the answer.

3. Run a small set of realistic sessions. Agentplace suggests covering these:

   * A typical customer who gives the expected information.
   * A vague request that needs clarifying questions.
   * A customer who changes a requirement after seeing a result.
   * Missing, conflicting or unsupported information.
   * A disconnected app, or an action that cannot complete.
   * Two customers whose private information must stay separate.

4. Add three cases that matter for any public agent: an emergency, an attempt to override the rules, and a question about something the agent should not know.

5. Check the page and the action. If the agent says it sent an email or booked a call, confirm that in the connected system.

6. Mark each answer pass or fail, and note why.

7. Fix one cause at a time. Retest the same questions in fresh sessions.

8. Keep your screenshots in pairs, before and after.

Use :doc:`the ten question set <../reference/test-questions>` if you want a ready made list.

A simple log
------------

.. list-table::
   :header-rows: 1
   :widths: 15 25 15 10 35

   * - Date
     - Question
     - Model
     - Result
     - Note
   * - 2 Nov 2026
     - Cheapest place in Kampala
     - GPT-6 Luna
     - Fail
     - Named a hotel and missed three cheaper homes.

Do not treat a good looking preview as proof that a real payment, booking or handoff worked.
