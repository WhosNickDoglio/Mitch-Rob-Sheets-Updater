#!/bin/bash

REPORT=`python -m redacted.redacted_covid_roster_check ${{ secrets.YAHOO_CLIENT_ID }} ${{ secrets.YAHOO_CLIENT_SECRET }} ${{ secrets.YAHOO_REFRESH_TOKEN }}`