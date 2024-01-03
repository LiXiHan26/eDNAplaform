
from django.contrib import admin
from django.urls import path, include  # add this
from .views import get_cos_credentials, MapView
from .views import NcbiDownloadDataView,EmblDownloadDataView, MitofishDownloadDataView, BoldDownloadDataView
from .views import FastaFileMergeDataView, FastaFileCleanDataView, FastaFileExportDataView, get_taxonomy, inslicoPCRView, pgaView, FastaFileDereplicateDataView, FastaFileAssignTaxDataView
from .views import HomeView,BookListView,BookCreateView,BookDeleteView,BookDetailView,BookUpdateView
from .views import CategoryListView,CategoryCreateView,CategoryDeleteView
from .views import PublisherListView,PublisherCreateView,PublisherDeleteView,PublisherUpdateView
from .views import ActivityListView,ActivityDeleteView
from .views import MemberCreateView,MemberUpdateView,MemberDeleteView,MemberListView,MemberDetailView
from .views import ProfileDetailView,ProfileCreateView,ProfileUpdateView
from .views import SequenceListView, SequenceCreateView, SequenceDetailView, SequenceUpdateView, SequenceDeleteView, SequenceCreateImportView
from .views import PrimersCreateView,PrimersListView, PrimersDeleteView
from .views import VisualizationDiversityView, VisualizationAmpliconView, VisualizationPhyloView, VisualizationCompletenessView, VisualizationPrimerEfficiencyView
from django.conf.urls.static import static
from .views import BorrowRecordListView,BorrowRecordCreateView,BorrowRecordDeleteView,BorrowRecordDetailView,auto_member,auto_book,BorrowRecordClose
from .views import DataCenterView,download_data, errors500, download_sequence
from .views import ChartView,global_serach,EmployeeView,EmployeeDetailView,EmployeeUpdate,NoticeListView,NoticeUpdateView

urlpatterns = [

    ##cos_credentials
    path('get-cos-credentials', get_cos_credentials, name='cos_credential'),
    path("download-sequence", download_sequence, name='download'),
    # HomePage
    path("",HomeView.as_view(), name='home'),
    #download_data
    path("ncbi-download-data",NcbiDownloadDataView.as_view(), name='ncbi_download_data'),
    path("ncbi-tax-update", get_taxonomy, name="ncbi_tax_update"),
    path("embl-download-data",EmblDownloadDataView.as_view(), name='embl_download_data'),
    path("mitofish-download-data",MitofishDownloadDataView.as_view(), name="mitofish_download_data"),
    path("bold-download-data",BoldDownloadDataView.as_view(), name='bold_download_data'),
    path("fasta-merge", FastaFileMergeDataView.as_view(), name='fasta_merge'),

    #dataProcess  
    path("inslico-pcr", inslicoPCRView.as_view(),name='inslico_pcr'),
    path("pga", pgaView.as_view(), name='pga'),
    
    #databases
    path("fasta-assign-tax", FastaFileAssignTaxDataView.as_view(), name='fasta_assign_tax'),
    path("fasta-dereplicate", FastaFileDereplicateDataView.as_view(), name='fasta_dereplicate'),
    path("fasta-clean", FastaFileCleanDataView.as_view(), name='fasta_clean'),
    path('fasta-export', FastaFileExportDataView.as_view() , name='fasta_export'),

    #Sequence
    path("sequence-list", SequenceListView.as_view(), name='sequence_list'),
    path("sequence-create", SequenceCreateView.as_view(), name='sequence_create'),
    path("sequence-create-import", SequenceCreateImportView.as_view(), name='sequence_create_import'),
    path('sequence-detail/<int:pk>/', SequenceDetailView.as_view(), name="sequence_detail"),
    path('sequence-update/<int:pk>/',SequenceUpdateView.as_view(),name="sequence_update"),
    path('sequence-delete/<int:pk>/',SequenceDeleteView.as_view(),name="sequence_delete"),

    #Primers
    path("primers-create", PrimersCreateView.as_view(), name='primers_create'),
    path("primers-list", PrimersListView.as_view(), name='primers_list'),
    path('primers-delete/<int:pk>/', PrimersDeleteView.as_view(), name="primers_delete"), 

    
    #Visualization
    path("visualization-diversity", VisualizationDiversityView.as_view(), name='visualization_diversity'),
    path("visualization-amplicon-length", VisualizationAmpliconView.as_view(), name='visualization_amplicon_length'),
    path("visualization-db-completeness", VisualizationCompletenessView.as_view(), name='visualization_db_completeness'),
    path("visualization-phylo", VisualizationPhyloView.as_view(), name='visualization_phylo'),
    path("visualization-primer-efficiency", VisualizationPrimerEfficiencyView.as_view(), name='visualization_primer_efficiency'),

    # Book
    path('book-list',BookListView.as_view(),name="book_list"),
    path('book-create',BookCreateView.as_view(),name="book_create"),
    path('book-update/<int:pk>/',BookUpdateView.as_view(),name="book_update"),
    path('book-delete/<int:pk>/',BookDeleteView.as_view(),name="book_delete"),
    path('book-detail/<int:pk>/',BookDetailView.as_view(),name="book_detail"),

    # Category
    path('category-list',CategoryListView.as_view(),name="category_list"),
    path('category-create',CategoryCreateView.as_view(),name="category_create"),  
    path('category-delete/<int:pk>/',CategoryDeleteView.as_view(),name="category_delete"), 

    # Publisher
    path('publisher-list',PublisherListView.as_view(),name="publisher_list"),
    path('publisher-create',PublisherCreateView.as_view(),name="publisher_create"),  
    path('publisher-delete/<int:pk>/',PublisherDeleteView.as_view(),name="publisher_delete"), 
    path('publisher-update/<int:pk>/',PublisherUpdateView.as_view(),name="publisher_update"),

    # User Activity
    path('user-activity-list',ActivityListView.as_view(),name="user_activity_list"),
    path('user-activity-list/<int:pk>/',ActivityDeleteView.as_view(),name="user_activity_delete"),

    # Membership
    path('member-list',MemberListView.as_view(),name="member_list"),
    path('member-create',MemberCreateView.as_view(),name="member_create"),  
    path('member-delete/<int:pk>/',MemberDeleteView.as_view(),name="member_delete"), 
    path('member-update/<int:pk>/',MemberUpdateView.as_view(),name="member_update"),
    path('member-detail/<int:pk>/',MemberDetailView.as_view(),name="member_detail"),

    # UserProfile
    path('user/profile-create/',ProfileCreateView.as_view(),name="profile_create"),
    path('user/<int:pk>/profile/',ProfileDetailView.as_view(),name="profile_detail"),
    path('user/<int:pk>/profile-update/',ProfileUpdateView.as_view(),name="profile_update"),


    # BorrowRecords
    path('record-create/',BorrowRecordCreateView.as_view(),name="record_create"),
    # path('record-create/',record_create,name="record_create"),

    path('record-create-autocomplete-member-name/',auto_member,name="auto_member_name"),
    path('record-create-autocomplete-book-name/',auto_book,name="auto_book_name"),
    path('record-list/',BorrowRecordListView.as_view(),name="record_list"),
    path('record-detail/<int:pk>/',BorrowRecordDetailView.as_view(),name="record_detail"),
    path('record-delete/<int:pk>/',BorrowRecordDeleteView.as_view(),name="record_delete"),
    path('record-close/<int:pk>/',BorrowRecordClose.as_view(),name="record_close"),

    # Data center
    path('data-center/',DataCenterView.as_view(),name="data_center"),
    path('data-download/<str:model_name>/',download_data,name="data_download"),

    # Chart
    path('charts/',ChartView.as_view(),name="chart"),

    #Map
    path('maps/',MapView.as_view(),name="map"),

    # Global Search
    path('global-search/',global_serach,name="global_search"),

    # Employee
    path('employees/',EmployeeView.as_view(),name="employees_list"),
    path('employees-detail/<int:pk>',EmployeeDetailView.as_view(),name="employees_detail"),
    path('employees-update/<int:pk>',EmployeeUpdate,name='employee_update'),

    # Notice
    path('notice-list/', NoticeListView.as_view(), name='notice_list'),
    path('notice-update/', NoticeUpdateView.as_view(), name='notice_update'),

    #errors
    path('errors-500', errors500, name='errors_500'),
]



