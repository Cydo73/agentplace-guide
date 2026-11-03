Findings
========

Independent findings from a stress test of an Agentplace travel agent. Written for the Agentplace team and for anyone building on the platform.

.. toctree::
   :maxdepth: 1

   results
   method

Summary
-------

I built a travel companion on Agentplace using public information from Tubayo, an African travel marketplace. I asked it ten questions around 1 November 2026 and compared its answers with those of Tubayo's own on site assistant.

* **Safety and honesty were strong.** The agent would not invent availability or promise refunds. For a gas leak report it told me to leave and call emergency services first.
* **Coverage was the weak point.** It missed items that were on the homepage: three homes at USD 34, Forest Cottages at USD 73 with breakfast, and a Skylar Homes listing.
* **It reached outside the site.** It quoted a price from Google Hotels and offered to help me book elsewhere, for a concept meant to stay inside one marketplace.
* **The site's own assistant had mixed results.** It knew some things the agent missed. It also gave availability, refund and hotel details that I could not support, and answered a gas leak report by telling me to contact the hotel.
* **One likely cause fits every miss.** Agentplace's documentation says the Builder starts with the homepage and does not keep syncing. I did not capture what the Builder imported, so I cannot confirm this, but it matches each item the agent missed.

What this means for Agentplace
------------------------------

These are suggestions from one tester, not a roadmap. I do not know what Agentplace has planned, and some of this may already exist.

1. **Show what an import actually read.** After a website is connected, list the pages and items the Builder used, with a date. The limit is documented, but if a builder cannot see what was read, it turns into a mystery. A visible list would make it a one minute check.

2. **Warn when a site looks like a catalog.** When an import finds a list of products or listings, say how many it found and suggest uploading a table if the site shows more. This is the exact gap behind the missed homes and hotels.

3. **Show which model answered.** I could not tell which model gave each answer. Agentplace says the agent switches to GPT-6 Luna when credits run out. Showing the active model beside each Preview answer would make test results trustworthy, especially for someone testing on a free plan.

4. **Offer a way to stay inside the sources.** The agent used Google Hotels data for a Tubayo concept. A clear setting, or a documented rule that holds, would help builders who need an agent that never speaks from outside its sources.

5. **Add a how to for structured catalogs.** Agentplace's documentation covers adding knowledge well. A short guide on turning a list of items into a table the agent can use would help the builders most likely to hit this problem. :doc:`Fix missing information <../how-to/fix-missing-information>` is my draft of one.

What worked well
----------------

* It declined to invent. Asked about availability it could not see, it said so and pointed to the booking calendar.
* It cited the platform's own terms on cancellation and promised no refund.
* For a double charge it drafted a handoff, kept payment details out, and said plainly that it was a draft and not sent.
* For a gas smell it gave safety steps first.
* Where it could not find a listing it asked me for the link instead of guessing.

What I could not check
----------------------

I could not verify several of the site assistant's claims, including a USD 27 listing, availability for December, and the Entebbe hotels. I mark them as unverified in the :doc:`results <results>`. I also did not record which model answered, and I ran each question once in what looks like a single long chat, so treat the results as a first look, not a measurement.

Next step
---------

I plan to add the listings table and the rules from this guide, then rerun the same questions in fresh sessions and publish the before and after. If you would like to see that, tell me which questions matter most to you.
