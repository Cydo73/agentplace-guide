Knowledge, instructions and handoffs
====================================

A wrong answer has one of three causes. Naming the cause tells you where to fix it, and fixing the wrong layer wastes time.

The three layers
----------------

.. list-table::
   :header-rows: 1
   :widths: 18 32 25 25

   * - Layer
     - What it holds
     - A failure looks like
     - The fix
   * - Knowledge
     - Facts: listings, prices, policies, examples.
     - The agent misses an item or states an old price.
     - Add or update the source. Say which one wins.
   * - Instructions
     - Rules: what to do, what never to do, how to behave when unsure.
     - The agent invents an answer, goes outside its sources, or assumes something.
     - Add or sharpen a rule, then test it.
   * - Handoffs
     - Where a case goes when the agent should not decide.
     - The agent tries to solve a refund, or says it sent something that it did not.
     - Connect a destination and confirm delivery.

Why the order matters
---------------------

If the agent lacks the fact, no rule can supply it. A rule can only tell the agent to admit the gap. If the agent has the fact but uses it badly, more data will not help, and a rule will. If the problem is a decision the agent should not make, neither fixes it, and a handoff does.

A worked example
----------------

I asked an agent for the cheapest place in Kampala. It named a hotel and missed three cheaper homes. That was a knowledge problem: the homes were not in its list. A new rule would not have found them. Adding the listings did.

I asked about a double charge. The agent produced a draft summary and told me where to send it, but it could not send anything. That is a handoff problem. Wording could not fix it. A connected destination with confirmed delivery could.

Wording is not enforcement
--------------------------

Agentplace advises that where approval is mandatory, you should build a workflow that enforces it, not rely only on what the prompt says. Rules shape behavior. Workflows guarantee it.
