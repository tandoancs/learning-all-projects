@ECHO OFF

REM #############################################################################################################################
REM #						BACKUP DATABASE PROGRAM SAVE TO LOCAL						#
REM #############################################################################################################################

REM START

REM set TIMESTAMP
set TIMESTAMP=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%
set TM=%TIME:~0,2%%TIME:~3,2%

REM set backup dir
set DIR=E:\BackupDB\

cd %DIR%

if not exist %TIMESTAMP%%TM% (
  REM create folder with today
  md %TIMESTAMP%%TM%
  
  cd E:\BackupDB\%TIMESTAMP%%TM%\
  if not exist BackupLog (
    md BackupLog
  )
  
)

set DIR=E:\BackupDB\%TIMESTAMP%%TM%\

REM cd to backup folder
cd E:\Program Files\MySQL\MySQL Server 5.7\bin

REM database

set one_dbs=au_avery_bn_plan_pfl au_avery_bn_plan_rfidht au_avery_bn_plan_rfidsb_new au_avery_bn_plan_thermal au_avery_bn_plan_thermal_pfl au_avery_bn_planning au_avery_bn_production au_avery_kh au_avery_kh_rfidht au_avery_lh_planning au_avery_oe au_avery_pc au_avery_pfl au_avery_production au_avery_rfidsb au_avery_thermal au_avery_thermal_pfl

set dbs=pc_avery_do_plan pc_avery_ppc pc_avery_production pc_avery_wms pc_intranet wh_avery wh_avery_fru wh_logistics pc_nbsz

REM tables

REM database pc_avery_do_plan
set tables1=ac_item_digital_varnish ac_item_os ac_machine ac_os_scan ac_os_scan_raw ac_output_raw ac_output_raw_dc ac_output_raw_miss ac_output_raw_total ac_paper_detail ac_paper_job ac_paper_raw ac_paper_setting ac_plan ac_plan_confirm ac_process_report ac_setting_date ac_setting_day ac_setting_hour ac_urgent_list ac_v1_plan automail_duplicate currency_code dc_plan digital_downtime_category digital_locator digital_plan digital_sheet digital_tracking film_lamination_plan foil_plan iot_tracking lamination_plan offset_hitrate_plan offset_hitrate_record offset_plan offset_sheet offset_tracking otk_information qc_master_file qc_rfht_check_list rbo_group rfid_checked_list temp_rfid_master_file uv_plan varnish_plan wh_hit_rate

REM database pc_avery_ppc
set tables2=db_basic db_error_code db_error_log db_logic db_menu db_menu_permission db_setup_speed db_setup_time db_user_login htl_auto_batching htl_auto_batching_color htl_auto_batching_size htl_auto_batching_size_del htl_auto_batching_txt_data htl_batching_build_stock_size htl_batching_step htl_build_fapl htl_build_sample htl_build_stock htl_build_wip htl_inbu htl_left_menu htl_master_file htl_message htl_mla htl_size htl_soline jj_left_menu jj_message mrp_actual_use_with_bl mrp_basic mrp_booked_number_tm_pfl mrp_booked_number_trims_sip_new mrp_booked_number_vips_new mrp_change_material mrp_forecast_data_draft mrp_holiday_setting mrp_item_master_data mrp_material_onhand mrp_material_output mrp_offset_alternative_materials mrp_offset_booked_rm_pivot mrp_offset_build_stock mrp_offset_convert_uom mrp_offset_item_scrap mrp_offset_outsource_so_line mrp_offset_process mrp_offset_process_rm_backup_day mrp_oracle_auto_mail_data mrp_planner_forecast mrp_planner_forecast_bl4 mrp_planner_forecast_bl5 mrp_planner_forecast_glid mrp_planner_forecast_glid_pivot mrp_planner_forecast_new mrp_pr_records mrp_process_rm mrp_sale_time mrp_setting_locked_bl mrp_setting_material_forecast_base_view mrp_sfc_confidence mrp_soh_data mrp_stock_flow_master_data mrp_target_inventory mrp_upload_excel_info mrp_user_permission mrp_user_permission_view ppc_diecut_report_process_type ppc_plan_cut_string ppc_plan_cut_string_production_confirm_stock ppc_plan_cut_string_received ppc_plan_cut_string_stock_on_shopfloor ppc_plan_cut_string_stock_on_shopfloor_auto_mail

REM database pc_avery_production
set tables3=calculator_config_information calculator_output_raw calculator_plan dat_history die_mold_warning dm_item_information hr_digital_machine lc_information lc_routine mold_locator mold_mail_address mold_mail_detail mold_mail_information mold_mail_material mold_mail_setting mold_master_file mold_setting mold_tracking ooh_d0 ooh_detail ooh_detail_raw ooh_history ooh_information ooh_spm_information ot_data ot_worker rm_detail rm_information spm_labour_date spm_labour_raw warning_information wh_receiving_detail

REM database pc_avery_wms
set tables4=wms_dn_information wms_information wms_raws

REM database pc_intranet
set tables5=intranet_menu intranet_menu_rfht intranet_permission intranet_user

REM database wh_avery
set tables6=cs_contact_list cs_dn_sent cs_pi_sent db_account db_contact db_dept dn_file dn_masterdata fg_poincoming fg_poincoming_barcode fg_poincoming_contact fg_poincoming_gridmain gridmain ic_supplier intranet_menu intranet_permission intranet_user intranet_user_fg item_carton link_log menu menuchildren oe_vips_information oe_vips_list_get oe_vips_material_map oe_vips_user pi_file pi_masterdata pkl_detail pkl_file pur_daily_tracking pur_daily_tracking_log pur_daily_tracking_tmp pur_dailytracking_contact pur_pr_pdl pur_rm_history_plan pur_rm_report_po_eta pur_rm_report_po_pending pur_rm_report_po_pending_detail pur_rm_report_thermal_eta pur_send_delay pur_tygia purchase_po purchase_po_total rm_adjustment_tracking rm_adjustment_tracking_approve rm_adjustment_tracking_barcode_inactive rm_adjustment_tracking_cyclecount_qtyonhand rm_adjustment_tracking_inbound_infochange rm_label_cycle_count rm_label_in rm_label_in_out rm_label_move rm_master_item_pdl rm_pnk_detail rm_pnk_id rm_poincoming rm_poincoming_contact rm_poincoming_lay_ngang rm_poincoming_log rm_poincoming_plan rm_poincoming_pnk scan_pl shipment_total shipment_total_fru shipment_total_kh site sp_backlog_onhand thermal_rm_bom version_software wh_cs_urgent wh_ordertracking wh_packing_list_label wh_packing_list_label_non_seq wh_vmi_material wh_xnk_in wh_xnk_in_draf wh_xnk_out wh_xnk_out_draf wh_xnk_pic wh_xnk_prekit_in wm4_preprint wm4_received_item_label wm4_scan_out wm_carton wm_carton_request_contact wm_carton_request_detail wm_carton_request_id wm_chemical_label wm_combinebox wm_cycle_count wm_dashboard_status wm_dn_backlog wm_dn_in wm_dn_in_log wm_dn_scan wm_master_category wm_master_locator wm_master_subinventory wm_master_uom wm_packinglist_dn wm_pallet wm_picker_warehouse wm_pxk_detail wm_pxk_information wm_pxkrm_detail wm_pxkrm_information wm_pxkrm_pallet wm_received_item_label wm_request_contact wm_request_detail wm_request_id wm_request_material_list wm_request_picklist wm_return_contact wm_return_request_detail wm_return_request_id wm_rm_onhand wm_shipment_manual wm_stock_contact wm_stock_onhand wm_stock_request_detail wm_stock_request_id wm_stock_request_picklist wm_trans_dn wm_trans_scan xnk_bill

set tables7=fg_poincoming fg_poincoming_barcode fg_poincoming_log intranet_permission intranet_user intranet_user_fg pkl_contact pkl_detail pkl_dn_confirm pkl_id pkl_pnk_remark pl_detail purchase_po purchase_po_total wh_ordertracking wh_packing_list_label wh_packing_list_label_non_seq wm_combinebox wm_cycle_count wm_dn_backlog wm_dn_in wm_dn_scan wm_packinglist_dn wm_picker_warehouse wm_pxk_detail wm_pxk_information wm_shipment_manual

set tables8=auto_mail phieu_ra_cong phieu_ra_cong_nguoi_dung phieu_ra_cong_tai_san_hang_hoa transport_config transport_customer transport_freight_out transport_invoice transport_lading_detail transport_lead_time transport_logs transport_netco_bay_tiet_kiem transport_netco_delivery_before_12_oclock_fee transport_netco_delivery_before_16_oclock_fee transport_netco_delivery_before_9_oclock_fee transport_netco_dtd_xe_tai_lon_fee transport_netco_dtd_xe_tai_nho_fee transport_netco_express_delivery_fee transport_netco_offline transport_netco_po_truck_delivery_fee transport_netco_road_72_hours_fee transport_netco_road_eco_fee transport_netco_tuyen_khoang_cach transport_netco_xe_may_fee transport_province transport_user transport_vintrans_delivery_before_12_oclock_fee transport_vintrans_delivery_before_16_oclock_fee transport_vintrans_delivery_before_9_oclock_fee transport_vintrans_dtd_xe_tai_lon_fee transport_vintrans_dtd_xe_tai_nho_fee transport_vintrans_express_delivery_fee transport_vintrans_ht_fee transport_vintrans_offline transport_vintrans_po_truck_delivery_fee transport_vintrans_road_72_hours_fee transport_vintrans_road_eco_fee transport_vintrans_toan_trinh_nhan_phat transport_vintrans_tuyen_khoang_cach wms_ship_work wms_ship_work_detail

set tables9=pkl_detail pkl_information

REM set Log file
set logFile="%DIR%BackupLog\log.%TIMESTAMP%%TM%.txt"

REM some database backup full one
(for %%d in (%one_dbs%) do (

    REM set timestamp and time to save log file
    set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
    set TM=%TIME:~0,2%%TIME:~3,2%
    
    REM save to dirLog
    ECHO "Backup Database %%d success %TIMESTAMP% %TM%" >> %logFile%
    
    REM backup with mysqldump: backup database user
    mysqldump --user=backupDB --password=BKAutomation{2020} --databases %%d > "%DIR%dump.%%d.%TIMESTAMP%%TM%.sql"
))


REM some database backup part
(for %%d in (%dbs%) do (

	REM pc_avery_do_plan tables1
	if "%%d" == "pc_avery_do_plan" (

		(for %%t in (%tables1%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM pc_avery_ppc tables2
	if "%%d" == "pc_avery_ppc" (

		(for %%t in (%tables2%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM pc_avery_production tables3
	if "%%d" == "pc_avery_production" (

		(for %%t in (%tables3%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM pc_avery_wms tables4
	if "%%d" == "pc_avery_wms" (

		(for %%t in (%tables4%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM pc_intranet tables5
	if "%%d" == "pc_intranet" (

		(for %%t in (%tables5%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM wh_avery tables6
	if "%%d" == "wh_avery" (

		(for %%t in (%tables6%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM wh_avery_fru tables7
	if "%%d" == "wh_avery_fru" (

		(for %%t in (%tables7%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

	REM wh_logistics tables8
	if "%%d" == "wh_logistics" (

		(for %%t in (%tables8%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

    REM pc_nbsz tables9
	if "%%d" == "pc_nbsz" (

		(for %%t in (%tables9%) do (
			REM set timestamp and time to save log file
			set TIMESTAMP=%DATE:~10,4%:%DATE:~4,2%:%DATE:~7,2%
			set TM=%TIME:~0,2%%TIME:~3,2%
			
			REM save to dirLog
			ECHO "Backup Database %%d %%t success %TIMESTAMP% %TM%" >> %logFile%
			
			REM backup with mysqldump: backup database user
			mysqldump --user=backupDB --password=BKAutomation{2020}  %%d %%t > "%DIR%dump.%%d.%%t.%TIMESTAMP%.sql"
		
		))
	)

))

REM THE END
