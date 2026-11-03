Method
======

How I tested, and what limits the results.

What I tested
-------------

* An Agentplace agent I built as an independent travel companion, using public information from Tubayo.
* Tubayo's own on site assistant, for comparison.

Neither belongs to me. Tubayo did not take part, and Agentplace did not review this work.

How I tested
------------

* I asked both assistants the same ten questions, listed in the :doc:`test reference <../reference/test-questions>`.
* I saved each answer as text and, for key moments, as a screenshot.
* I took screenshots of the Tubayo homepage on 1 November 2026 to check prices and listings.
* I read Agentplace's public documentation on 2 November 2026 to understand what behavior is documented.

Limits
------

* **One run per question.** Language models can answer differently each time. These are first impressions, not measurements.
* **One long chat.** The answers refer back to earlier ones, which suggests I asked all ten in a single conversation, so earlier answers may have affected later ones. The gas emergency shaped the replies to questions 9 and 10.
* **Model not recorded.** I did not note which model answered each question. Agentplace says an agent switches to GPT-6 Luna when credits run out, so I cannot rule out a change during testing.
* **Credits.** My credit balance reached zero after testing. Agentplace says GPT-6 Luna stays free at zero credits, so I expect to be able to rerun the set on Luna.
* **Homepage only.** My checks come from the Tubayo homepage. I did not browse the See more pages, so some listings may exist that I did not see.
* **Tubayo's side not verified.** I did not confirm the assistant's availability, refund and Entebbe claims. The status column marks each one.
* **What the agent read.** I did not capture what the Builder imported from the site, so I cannot say exactly why items were missed. The explanation in :doc:`Why agents miss information <../explanation/why-agents-miss-information>` is a likely cause, not a confirmed one.

How to reproduce
----------------

1. Build the agent with the :doc:`tutorial <../tutorial/build-your-first-agent>`.
2. Run each question in a fresh session.
3. Record the model and the date.
4. Compare each answer with the live site.

Prices and listings change, so your results will differ from mine.

What I would do next
--------------------

Add the listings table and the rules, rerun the same questions in fresh sessions with a recorded model, and publish the before and after.
