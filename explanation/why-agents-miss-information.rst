Why agents miss information
===========================

An agent can sound sure and still be working from only part of your site. This page explains why that happens and what it means for how you build.

The Builder reads a start, not the whole site
---------------------------------------------

When you give the Builder a website, Agentplace says it starts with the homepage and a useful customer action, then expands as you refine the agent. Review other pages and tasks with it instead of assuming every page has been recreated.

Two further points from Agentplace's documentation matter here:

* Using a website at creation does not set up an ongoing sync. When something changes, you give the Builder the update.
* An uploaded copy is not necessarily a live feed. For prices and availability that change, you decide whether the agent reads a connected source or a reference you keep updated.

Content that loads after the page opens
---------------------------------------

Many sites build their lists after the page opens, using scripts. When I fetched the Tubayo homepage as plain text, I got the page title and description, not the stays and experiences a browser shows. I do not know whether the Builder reads pages the same way, so treat this as a likely cause rather than a confirmed one. It is a good reason to check what your agent actually has.

Why a partial view produces a confident wrong answer
----------------------------------------------------

An agent that filters well can still give the wrong answer if its list is short. Asked for hotels under a budget with breakfast, it will correctly pick from the items it holds. If it holds three of ten, it may name one as the only option. The reasoning was sound. The data was not.

That is why completeness matters more than clever wording. A rule such as "say how many you found, and never call a result the only one unless the list is complete" does two jobs. It stops false claims, and it makes the gap visible to you when you test.

What this means for how you build
---------------------------------

* Put the items you care about in a table you control.
* Say which source wins when sources disagree.
* Tell the agent to admit what it cannot confirm.
* Test with questions where the right answer is on a deeper page.
* Date your data, and update it when the business changes.

See :doc:`Fix missing information <../how-to/fix-missing-information>` for the steps.
