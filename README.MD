# 🪙 Day 41 — Reddit Top 10 Posts Viewer

## 📖 Overview
For **Day 41** of my *100 Days, 100 Projects in Python* challenge, I built a **Reddit Top 10 Posts Viewer**!  
This Python script fetches the **Top 10 trending posts** from Reddit (either from `r/all` or any specific subreddit) and displays their titles, upvotes, and links right in the terminal 🔥  

No API key required — it uses Reddit’s public JSON API.

---

## ⚙️ Features
✅ Fetches top 10 Reddit posts of the day  
✅ Works for any subreddit (default: `r/all`)  
✅ Displays post title, upvotes, and direct link  
✅ Simple and fast — no authentication needed  

---

## 🧩 Requirements
Install the required library:
```bash
pip install requests
💻 How to Run
Clone or download this project.

Open a terminal in the project directory.

python reddit_top10.py
Enter a subreddit name (or press Enter for r/all).

🧠 Example Output

Enter subreddit (or leave blank for 'all'): 

🔥 Top 10 Posts on r/all (Past 24h)
--------------------------------------------------
1. Trump and friends feast hours before cutting SNAP benefits. "May the odds be ever n your favor." (83657 upvotes)
   🔗 https://reddit.com/r/pics/comments/1olq5s2/trump_and_friends_feast_hours_before_cutting_snap/

2. Ohio couple with the same birthday give birth to twins on their birthday. The whole family has the same birthday. (72728 upvotes)
   🔗 https://reddit.com/r/interestingasfuck/comments/1olm8xy/ohio_couple_with_the_same_birthday_give_birth_to/

3. Amazing shop owner helping kids to do good (72878 upvotes)
   🔗 https://reddit.com/r/MadeMeSmile/comments/1olnrqv/amazing_shop_owner_helping_kids_to_do_good/

4. Brazilian bin man during Halloween (70476 upvotes)
   🔗 https://reddit.com/r/MadeMeSmile/comments/1olnj35/brazilian_bin_man_during_halloween/

5. That's a pretty cool dinosaur costume! (59436 upvotes)
   🔗 https://reddit.com/r/nextfuckinglevel/comments/1olmh61/thats_a_pretty_cool_dinosaur_costume/

6. The Danish Foreign Minister gifts the Egyptian Foreign Minister a Pyramid Lego set. (53495 upvotes)
   🔗 https://reddit.com/r/MadeMeSmile/comments/1olsqck/the_danish_foreign_minister_gifts_the_egyptian/

7. annual NYC Halloween parade (53025 upvotes)
   🔗 https://reddit.com/r/nextfuckinglevel/comments/1oltu9u/annual_nyc_halloween_parade/

8. Dancers at Trump’s Halloween party as people begin losing food stamps under his administration (52336 upvotes)
   🔗 https://reddit.com/r/CringeTikToks/comments/1olu5op/dancers_at_trumps_halloween_party_as_people_begin/

9. Happy Halloween (52169 upvotes)
   🔗 https://reddit.com/r/funny/comments/1oln8zd/happy_halloween/

10. [OC] Went to a halloween party with my partner as Kim Possible and Rufus (55893 upvotes)
   🔗 https://reddit.com/r/pics/comments/1om5dae/oc_went_to_a_halloween_party_with_my_partner_as/
