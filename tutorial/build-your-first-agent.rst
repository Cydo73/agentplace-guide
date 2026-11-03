Build and publish your first Agentplace agent
=============================================

By the end of this tutorial you will have a published agent with its own link. The example is a travel companion that helps a traveler plan a trip and answers questions about bookings.

The example uses public information from Tubayo, an African travel marketplace. It is an independent concept, not an official Tubayo product. You can swap in any business you know well.

What you need
-------------

* An email address to create an Agentplace account. You can start free.
* A website to build from. This tutorial uses ``https://www.tubayo.com``.
* A table of the items your agent should know about. :doc:`The sample table <../reference/sample-listings>` shows the format.
* About an hour. Most of it goes on testing, not building.

Agentplace says GPT-6 Luna is always free in the Builder and in your agent, even when your credit balance is zero. This tutorial uses that model, so you should not need to pay.

Step 1. Open the workspace and sign in
--------------------------------------

Go to ``agentplace.io`` and open the workspace. Sign in or create an account.

*Why:* the workspace is where the Builder lives. The Builder is the AI that helps you create and change your agent.

.. image:: /_static/screenshots/step-01-signup.png
   :alt: The Agentplace sign in page.
   :width: 90%

Step 2. Find your dashboard
---------------------------

After you sign in you land on your dashboard. Find the option to create a new agent.

*Why:* you will come back here to reopen, edit and publish your agents, so it helps to know where it is.

.. image:: /_static/screenshots/step-02-dashboard.png
   :alt: The Agentplace dashboard with the option to create a new agent.
   :width: 90%

Step 3. Start a new agent
-------------------------

Choose to start from your own idea. You can also start from a template, but a template only opens the workspace with a business brief. It does not create an agent for you.

*Why:* starting from your own idea makes you decide what the agent is for, which is the hardest and most useful part.

.. image:: /_static/screenshots/step-03-create-agent.png
   :alt: The screen where you choose to start from an idea or a template.
   :width: 90%

Step 4. Describe who will use it and what they should do
--------------------------------------------------------

Send the Builder your first message. Say who the users are and what they should be able to accomplish. Paste this, or write your own version:

.. code-block:: text

   Create an independent travel companion agent based on the public Tubayo
   website at https://www.tubayo.com. It is a concept build, not an official
   Tubayo product. Travelers should be able to tell me where, when, how many
   people and what budget, and get matching stays and experiences with a short
   itinerary and an estimated cost. The agent should also answer questions
   about payments, cancellations, changes and refunds using only published
   policies. Use the listings file I will upload as the source of truth for
   stays. If something is not in your sources, say you cannot confirm it and
   point to the relevant Tubayo page. Hand off to a person for refunds, failed
   payments, complaints and any safety issue.

*Why:* the Builder does not know your business until you tell it. A clear user and a clear result stop it from guessing the scope. Naming what happens when information is missing sets the right behavior from the start.

.. image:: /_static/screenshots/step-04-name-and-describe.png
   :alt: The first message to the Builder describing the travel companion.
   :width: 90%

Step 5. Choose the model
------------------------

Open the model setting for your agent and choose GPT-6 Luna.

*Why:* it is free at every credit level, so your tests cost nothing. When credits run out on a paid model, your agent switches to Luna automatically. Choosing Luna from the start means the model does not change in the middle of your testing.

.. image:: /_static/screenshots/step-05-select-model-luna.png
   :alt: The model setting with GPT-6 Luna selected.
   :width: 90%

Step 6. Give the agent its rules
--------------------------------

Tell the Builder the rules the agent must follow. Paste this block:

.. code-block:: text

   Use only Tubayo listings and Tubayo's displayed prices. Never quote prices
   from other sites or suggest booking elsewhere. When a traveler gives
   filters such as price, area or breakfast, check every listing in your
   knowledge before answering. List all that match, up to five, and say how
   many you found. Use prices exactly as shown on Tubayo, without converting
   currencies unless asked. Never say a result is the only option unless you
   are sure your listings are complete. Say "from the listings I have" and
   point to the Tubayo search page for more. Only suggest listings in the
   city the traveler asked about. If a listing is missing from your
   knowledge, say so and ask for the link. For trip plans, give a draft
   itinerary with a cost estimate, label what is unconfirmed, and ask for
   dates afterwards. Never assume anything the traveler has not said,
   including their safety or location. For a safety emergency, tell the
   traveler to get to safety and call local emergency services first, then
   offer to notify Tubayo.

*Why:* each rule closes a specific gap. :doc:`Set rules for your agent <../how-to/set-rules-for-your-agent>` explains what each one prevents.

.. image:: /_static/screenshots/step-06-write-instructions.png
   :alt: The rules block sent to the Builder.
   :width: 90%

Step 7. Add your knowledge
--------------------------

Give the Builder the website address and upload your listings table. Then say which source wins if they disagree. Paste this:

.. code-block:: text

   The attached listings file is the source of truth for stays and prices.
   The Tubayo website is a reference for policies and descriptions. If they
   disagree, use the file and tell the traveler the website may differ.

*Why:* the Builder starts with the homepage and a useful customer action, then expands as you refine. It does not read every page by default, and an uploaded copy is not a live feed. A table you control fills the gap, and naming the winning source prevents confusion when two sources disagree.

.. image:: /_static/screenshots/step-07-add-website-knowledge.png
   :alt: The website address and listings file added as knowledge.
   :width: 90%

Step 8. Test in Preview
-----------------------

Open Preview and run these six questions. Use a fresh session for each one if you can.

1. "Cheapest place in Kampala, any type."
2. "Hotel in Kampala under $80 with breakfast, near Naguru or Bukoto."
3. "Is the Evara bnb available December 20 to 27?"
4. "What is your cancellation policy? If I cancel 3 days before, do I get a full refund?"
5. "I was charged twice for my booking."
6. "I'm at a hotel and there's a gas smell."

Check each answer against your table and your rules. Ask the Builder to fix anything that is wrong, in plain language.

*Why:* a preview that looks right is not proof that it is right. Realistic questions, including missing information and emergencies, find the problems a typical question hides. :doc:`The test reference <../reference/test-questions>` has ten questions and what a safe answer looks like.

.. image:: /_static/screenshots/step-08-test-in-preview.png
   :alt: A test question and the agent's answer in Preview.
   :width: 90%

Step 9. Publish
---------------

Start the publish flow and choose who can use the agent:

* **Public** lets anyone with the link use it.
* **Restricted** limits it to specific email addresses or domains.
* **Private** keeps it for you.

For a public demo, choose Public. For a public agent you also choose whether visitors must sign in and whether others may duplicate your agent. Leave duplication off unless you want people to copy it. Then complete the flow.

*Why:* your working Preview and your published agent are separate. Nothing reaches visitors until you publish.

.. image:: /_static/screenshots/step-09-publish.png
   :alt: The publish screen with access options.
   :width: 90%

Step 10. Test the live link
---------------------------

Open the published link in a private browser window, so you are not signed in as the owner. Ask two of your test questions and open it on a phone.

*Why:* the live agent can behave differently from the preview. Testing as a visitor is the only way to know what a customer sees.

.. image:: /_static/screenshots/step-10-live-agent.png
   :alt: The published agent answering a question at its own link.
   :width: 90%

Recap
-----

You now have an agent with a clear job, a model that costs nothing, rules that close known gaps, a knowledge table you control, and a link a visitor can use. You also tested it as both the owner and a visitor.

If an answer is wrong or incomplete, go to :doc:`Fix missing information <../how-to/fix-missing-information>`. To see what I found when I stress tested this exact agent, read the :doc:`findings <../findings/index>`.
