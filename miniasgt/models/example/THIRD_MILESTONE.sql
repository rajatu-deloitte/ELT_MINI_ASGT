SELECT BODY FROM POST INNER JOIN USERS ON POST.OWNERUSERID = USERS.ACCOUNTID WHERE USERS.DISPLAYNAME like '%nau%' AND POST.POSTTYPEID=1