# python



## todo

  + LA
    - LA_base src

  + Data Science


## doing

  + practice_python LIST


## done

  + LA
    - ~~html : find out a way of showing popup txt~~

```
                [new Date(2010,8,1,12,0,0), , '<div title="Actual: popup_report"> my_Report </div><br>' +
                        '<img src="img/attachment-icon.png" style="width:32px; height:32px;">']
```


## idea

  + Log Analayzer (LA)

  
    + LA 
      - in : key_word  file 
      - in : proc_**  excute environment / log_type
      - in : log_dirs , zip file
      - out : execute  proc_**
      - task : get hash-value (sha1sum),  unzip file, list files, execut proper proc_** program
      
    
    + proc_main
      - in : key_word file
      - in : req_type (file_type : ex> main, radio, system)
      - in : log_files
      - out : timeline_**
    
    + `Data` key_word
      - FORMAT : log_type, tag_id, search_word, show_msg, icon_id
      
    + `Data` proc_parsing_type.cfg
      - FORMAT : log_type, file_name, proc_name, shell_name, envir_para
      
    + `Data` timeline_**
      - FORMAT : st_time, ed_time, show_msg[= tag_id +'--' + search_word], icon_id, tag_id, full_msg
      
    + `Data` icon.cfg
      - FORMAT : icon_id, icon_html_txt
