Set up a handoff to a person
============================

**Last checked:** |last_checked| against Agentplace's public documentation.

Use this guide when your agent should pass a case to your team instead of answering it.

Before you start
----------------

You need somewhere for the handoff to go, such as an email address, a calendar or a CRM. A handoff with no connected destination cannot be completed.

Steps
-----

1. List the cases that need a person. For a travel agent these are refunds, failed or double payments, host complaints, safety issues and anything the agent cannot verify.

2. Decide what the handoff carries: the traveler's request, the booking reference, what has already been explained, what is unresolved, and the next action. Include only what the recipient is allowed to see.

3. Connect the destination and tell the Builder to use it.

4. Tell the agent to confirm delivery before it says the case has been handed over. If delivery fails, it should say what remains unfinished and offer another route.

5. Test the paths that go wrong: a destination that is unavailable, a request that is declined, and one that nobody answers.

A handoff summary
-----------------

.. code-block:: text

   Issue: Traveler reports being charged twice for one booking.
   Booking reference: [from traveler]
   Charge dates and amounts: [from traveler]
   Already explained: The agent cannot reverse charges or promise a refund.
   Next action: Review the charges and reply to the traveler.

Never ask the traveler for card numbers, security codes or passwords in chat.

Safety comes first
------------------

If someone reports danger, such as a gas smell, the agent should tell them to get to safety and call local emergency services before it does anything else. A handoff to your team comes second.

Check that it worked
--------------------

* The agent says "sent" only after delivery is confirmed.
* A draft that was not sent is called a draft.
* The person receiving the case does not need to ask the traveler to start again.
