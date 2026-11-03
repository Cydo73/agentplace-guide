Fix missing information
=======================

**Last checked:** |last_checked| against Agentplace's public documentation.

Use this guide when your agent leaves out items you can see on the website, or says it cannot find something that exists.

Before you start
----------------

You need a question the agent answered badly, and the right answer from the live site.

Steps
-----

1. Save the bad answer first. Take a screenshot with the question visible. You will need it to show the fix worked.

2. Check whether the item is on the homepage or deeper. Content loaded after the page opens, such as a list that appears when you scroll, may not be read the way a plain page is.

3. Put the items in a table you control. Use one row per item with the same columns every time. Name, type, area, price, and any filter your travelers use, such as breakfast. Save it as a CSV file. :doc:`The sample table <../reference/sample-listings>` shows the format.

4. Put today's date at the top of the file, or in the file name, for example ``listings_2026-11-02.csv``.

5. Upload the file to your agent and tell the Builder which source wins:

   .. code-block:: text

      The attached file is the source of truth for items and prices.
      If the website disagrees, use the file and say the website may differ.

6. Add the fallback rule:

   .. code-block:: text

      If something is not in your sources, say you cannot confirm it,
      point to the relevant page, and offer a person.

7. Ask the original question in a fresh session. Compare the new answer with your screenshot.

8. Publish again. A fix in Preview does not reach visitors until you publish the update.

Check that it worked
--------------------

* The agent lists every matching item, not only one.
* It says how many it found.
* It never says an item is the only option unless the table is complete.
* It names the item you could not find before.

If a listing is still missing, check the table first. The agent can only use what the table contains.
