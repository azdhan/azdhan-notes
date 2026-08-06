I have a LinkedIn analytics raw data file in markdown format. Each post's data is structured as shown in the example below.

Please parse the entire file and arrange all posts into a **single comprehensive table** with the following columns:

| Column Name         | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| Post #              | Sequential number of the post                                                      |
| Author              | Name of the LinkedIn post author                                                   |
| Post Content (Full) | The complete text of the post (including any emojis, hashtags, and call-to-action) |
| Impressions         | Total impressions                                                                  |
| In‑network %        | Percentage of impressions from in‑network                                          |
| Out‑of‑network %    | Percentage of impressions from out‑of‑network                                      |
| Members Reached     | Total unique members reached                                                       |
| Profile Viewers     | Number of profile viewers from this post                                           |
| Followers Gained    | Number of followers gained from this post                                          |
| Reactions           | Total reactions (likes, etc.)                                                      |
| Comments            | Total comments                                                                     |
| Reposts             | Total reposts/shares                                                               |
| Saves               | Total saves                                                                        |
| Sends               | Total sends on LinkedIn                                                            |
| Top Seniority       | Top seniority level with percentage                                                |
| Top Industry        | Top industry with percentage                                                       |
| Top Company Size    | Top company size with percentage                                                   |
| Top Location        | Top location with percentage                                                       |
| Top Job Title       | Top job title with percentage                                                      |
| Top Company         | Top company with percentage                                                        |

**Important Rules:**
1. Extract data exactly as shown — do not summarize or truncate the post content.
2. Keep percentages in the format shown (e.g., "34%", "22%").
3. For demographics, include both the label and percentage (e.g., "Senior (34%)").
4. If any field is missing or not applicable, leave it blank.
5. The final output should be a clean markdown table ready to copy-paste into Excel.
6. Add a "Post #" column as the first column for easy reference.

Here is the raw data file content:

[PASTE YOUR FULL MD FILE CONTENT HERE]