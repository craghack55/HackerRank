select cont.contest_id, cont.hacker_id ,cont.name, sum(nvl(sust.total_submissions, 0)),
                                                   sum(nvl(sust.total_accepted_submissions, 0)),
                                                   sum(nvl(vist.total_views, 0)),
                                                   sum(nvl(vist.total_unique_views, 0))
from Contests cont, Colleges coll, Challenges chal,
    (select vist.challenge_id, sum(vist.total_views) total_views, sum(vist.total_unique_views) total_unique_views
       from View_Stats vist
       group by vist.challenge_id) vist,
       (select sust.challenge_id, sum( sust.total_submissions) total_submissions,
               sum(sust.total_accepted_submissions) total_accepted_submissions
       from Submission_Stats sust
       group by sust.challenge_id) sust
where cont.contest_id = coll.contest_id and coll.college_id = chal.college_id
    and chal.challenge_id = vist.challenge_id(+)
    and chal.challenge_id = sust.challenge_id(+)
group by cont.contest_id, cont.hacker_id, cont.name
having sum(nvl(sust.total_submissions, 0)) > 0 or
       sum(nvl(sust.total_accepted_submissions, 0)) > 0 or
       sum(nvl(vist.total_views, 0)) > 0 or
       sum(nvl(vist.total_unique_views, 0)) > 0 or
order by cont.contest_id;