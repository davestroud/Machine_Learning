.selectExpr(
    'dl_load_dttm as date',
    'Id',
    'Job_Auto_Number__c as client_contact_id',
    'TR1__Open_Date__c as jo_date_added',
    'Posting_Start_Date__c as jo_date_start',
    'Posting_End_Date__c as jo_date_end',
    'Contract_Hours__c as jo_hours_per_week',
    'TR1__Number_of_Openings as jo_num_openings',# missing all
    #'payrate as jo_pay_rate', looking into this
    #'clientbillrate as jo_client_bill_rate', looking into this
    # static features
    'OwnerId as recruiter_id',
    #'externalid',
    #'correlatedcustomtextblock2 as billcode_title',
    'Name',
    'City__c as raw_city',
    #'state as raw_state', missing 87% ~ doesnt appear to have the same relevance as US states
    #'durationweeks as jo_duration',
    #'onsite as jo_onsite',
    #'isinterviewrequired as jo_interview_required',
    'TR1__Post_Externally__c as jo_will_relocate', # this is a bit of a gamble, intuition based!!
)