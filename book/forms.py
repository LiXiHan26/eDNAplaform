from django import forms
from book import models
from .models import Book,Publisher,Member,Profile,BorrowRecord, NcbiDownloadModel,MitofishDownloadModel, Primers
from .models import Sequence
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django.core.validators import RegexValidator, ValidationError
from django.urls import reverse
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput


#Download Form
class NcbiDownloadDataForm(forms.ModelForm):
    Email_Address = forms.EmailField(label='邮箱',
                                     widget=forms.EmailInput(attrs={
                                         'placeholder': '输入你的合法邮箱',
                                         'type': 'email',
                                     })
                                     )
    Database = forms.ChoiceField(label='数据库名称',
                                 choices=models.NCBI_Database_list,
                                 widget=forms.Select(attrs={
                                     'class': 'form-select',
                                 }),
                                 )
    Query = forms.ChoiceField(label='区域',
                              choices=models.Query_list,
                              widget=forms.Select(attrs={
                                  'class': 'form-select',
                              }),
                              )
    Batch_Size = forms.IntegerField(label='单次下载数量',
                                    widget=forms.NumberInput(attrs={
                                        'value': '5000',
                                        'step': '1000',
                                        'readonly': True,
                                    })
                                    )
    OriginalDownloadFile = forms.BooleanField(label='保存源文件',
                                              widget=forms.CheckboxInput(attrs={
                                                  'checked': 'checked',
                                              })
                                              )
    SpeciesFile = forms.FileField(label='物种名录文件上传',
                                  widget=forms.FileInput(attrs={
                                      'multiple': '',
                                      'accept': '.txt',
                                  })
                                  )
    
    class Meta:
        model = NcbiDownloadModel
        fields = ('Email_Address',
                  'Database',
                  'Query',
                  'Batch_Size',
                  'OriginalDownloadFile',
                  'SpeciesFile')

class EmblDownloadDataForm(forms.Form):
    Database = forms.ChoiceField(label='数据库名称',
                                 choices=models.EMBL_Database_list,
                                 widget=forms.Select(attrs={
                                     'class': 'form-select',
                                 }),
                                 )
    OriginalDownloadFile = forms.BooleanField(label='保存源文件',
                                              widget=forms.CheckboxInput(attrs={
                                                  'checked': 'checked',
                                              })
                                              )

class MitofishDownloadDataForm(forms.ModelForm):
    OriginalDownloadFile = forms.BooleanField(label='保存源文件',
                                              widget=forms.CheckboxInput(attrs={
                                                  'checked': 'checked',
                                              }))

    class Meta:
        model = MitofishDownloadModel
        fields = ('__all__')

class BoldDownloadDataForm(forms.Form):
    Database = forms.FileField(label='物种名录文件上传',
                                widget=forms.FileInput(attrs={
                                    'multiple': '',
                                    'accept': '.txt',
                                })
                                )
    OriginalDownloadFile = forms.BooleanField(label='保存源文件',
                                              widget=forms.CheckboxInput(attrs={
                                                  'checked': 'checked',
                                              })
                                              )

class FastaFileMergeDataForm(forms.Form):
    FastaFile = forms.FileField(label='Fasta文件上传',
                                  widget=forms.FileInput(attrs={
                                      'multiple': '',
                                      'accept': '.fasta',
                                  })
                                  )


#Fasta Process Form
    
class inslicoPCRForm(forms.Form):  
    Input_File = forms.FileField(label='源文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.fasta',
                                 })
                                 )
    Forword_Primer = forms.CharField(label='正向引物',
                                     widget=forms.TextInput(attrs={
                                         'required': True,
                                     })
                                     )
    Reverse_Primer = forms.CharField(label='反向引物',
                                     widget=forms.TextInput(attrs={
                                         'required': True,
                                     })
                                     )
    Error_Num = forms.FloatField(label='错误率',
                                 widget=forms.NumberInput(attrs={
                                     'placeholder': '默认值为4.5',
                                     'step': '0.5',
                                     'min': '0',
                                     'value': '4.5',
                                     'readonly': True,
                                 })
                                 )

class pgaForm(forms.Form):
    Input_File = forms.FileField(label='输入文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.fasta',
                                 })
                                 )
    Database_File = forms.FileField(label='数据库文件',
                                    widget=forms.FileInput(attrs={
                                     'accept': '.fasta',
                                 })
                                 )
    Forword_Primer = forms.CharField(label='正向引物',
                                     widget=forms.TextInput(attrs={
                                         'required': True,
                                     })
                                     )
    Reverse_Primer = forms.CharField(label='反向引物',
                                     widget=forms.TextInput(attrs={
                                         'required': True,
                                     })
                                     )
    Speed = forms.ChoiceField(label='下载速度',
                            choices=models.PGA_SPEED,
                            widget=forms.Select(attrs={
                                'required': True,
                                'class': 'form-select',
                            })
                            )
    Percid = forms.FloatField(label='Percid',
                            widget=forms.NumberInput(attrs={
                                'placeholder': '默认值为0.95',
                                'step': '0.1',
                                'min': '0',
                                'value': '0.95',
                                'readonly': True,
                            })
                            )
    Coverage = forms.FloatField(label='Coverage',
                                widget=forms.NumberInput(attrs={
                                    'placeholder': '默认值为0.95',
                                    'step': '0.1',
                                    'min': '0',
                                    'value': '0.95',
                                    'readonly': True,
                                })
                                )
    Filter_Method = forms.ChoiceField(label='筛选方法',
                                    choices=models.FILTER_METHOD,
                                    widget=forms.Select(attrs={
                                        'required': True,
                                        'class': 'form-select',
                                    })
                                    )


# database
class FastaAssignTaxDataForm(forms.Form): 
    Fasta_File = forms.FileField(label='Fasta文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.fasta',
                                 }),
                                 )
    

class FastaFileDereplicateDataForm(forms.Form):
    Tsv_File = forms.FileField(label='TSV文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 }),
                                 )
    Method = forms.ChoiceField(label='去重方法',
                                 choices=models.Dereplicate_Methods,
                                 widget=forms.Select(attrs={
                                     'class': 'form-select',
                                 }),
                                 )

class FastaFileCleanDataForm(forms.Form):
    Tsv_File = forms.FileField(label='TSV文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 }),
                                 )
    Seq_Length = forms.CharField(label='最大最小长度范围',
                                 widget=forms.TextInput(attrs={
                                     'class': '',
                                 }),
                                 )
    Num_Of_Ambiguous_Bases = forms.IntegerField(label='模糊序列数量',
                                                widget=forms.NumberInput(attrs={
                                                    'placeholder': '默认值为0'
                                                }),
                                                )
    Missing_Taxonomic_Information = forms.IntegerField(label='缺省值',
                                                       widget=forms.NumberInput(attrs={
                                                           'placeholder': '默认值为0'
                                                       })
                                                       )
    Environment_Seq = forms.CharField(label='环境序列',
                                      widget=forms.CheckboxInput(attrs={
                                          'checked': 'checked',
                                          'value': 'yes',
                                      }),
                                      )
    Unspecified_Name = forms.CharField(label='不确定物种命名',
                                       widget=forms.CheckboxInput(attrs={
                                           'checked': 'checked',
                                           'value': 'yes',
                                       }),
                                       )

class FastaFileExportDataForm(forms.Form):
    Tsv_File = forms.FileField(label='输入文件',
                               widget=forms.FileInput(attrs={
                                   'accept': '.tsv',
                               })
                               )
    Export_Type = forms.ChoiceField(label='导出格式',
                                    widget=forms.Select(attrs={
                                        'class': 'form-select',
                                        'data-placeholder': '选择格式',
                                    }),
                                    choices=models.Export_Type_List
                                    )


#Visualization Form
class VisualizationDiversityForm(forms.Form):
    Input_File = forms.FileField(label='输入文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 })
                                 )

    Bio_Classification = forms.ChoiceField(label='分类等级',
                                            choices=models.Biological_Classification,
                                            widget=forms.Select(attrs={
                                                'class': 'form-select',
                                            })
                                            )
    
class VisualizationAmpliconForm(forms.Form):
    Input_File = forms.FileField(label='输入文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 })
                                 )

    Bio_Classification = forms.ChoiceField(label='分类等级',
                                            choices=models.Biological_Classification,
                                            widget=forms.Select(attrs={
                                                'class': 'form-select',
                                            })
                                            )

class VisualizationCompletenessForm(forms.Form):
    Input_File = forms.FileField(label='输入文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 })
                                 )
    Species_File = forms.FileField(label='物种名录文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.txt',
                                 })
                                 )

class VisualizationPhyloForm(forms.Form):
    Input_File = forms.FileField(label='输入文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 })
                                 )
    Species_File = forms.FileField(label='物种名录文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.txt',
                                 })
                                 )
    Bio_Classification = forms.ChoiceField(label='分类等级',
                                            choices=models.Biological_Classification,
                                            widget=forms.Select(attrs={
                                                'class': 'form-select',
                                            })
                                            )

class VisualizationPrimerEfficiencyForm(forms.Form):
    Input_File = forms.FileField(label='输入文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.tsv',
                                 })
                                 )
    Forword_Primer = forms.CharField(label='上游引物',
                                     widget=forms.TextInput(attrs={
                                         'required': True,
                                     })
                                     )
    Reverse_Primer = forms.CharField(label='下游引物',
                                     widget=forms.TextInput(attrs={
                                         'required': True,
                                     })
                                     )
    Forword_Primer_Name = forms.CharField(label='上游引物名称',
                                            widget=forms.TextInput(attrs={
                                                'required': True,
                                            })
                                            )
    Reverse_Primer_Name = forms.CharField(label='下游引物名称',
                                            widget=forms.TextInput(attrs={
                                                'required': True,
                                            })
                                            )
    Raw_File = forms.FileField(label='序列文件',
                                 widget=forms.FileInput(attrs={
                                     'accept': '.fasta',
                                 })
                                 )
    Tax_Group = forms.CharField(label='分类类群名称',
                                widget=forms.TextInput(attrs={
                                    'required': True,
                                })
                                )


#sequence
class SequenceCreateEditForm(forms.ModelForm):
    class Meta:
        model = Sequence
        fields = ('__all__')

class SequenceCreateImportForm(forms.ModelForm):
    Sequence_Import = forms.FileField(label='输入文件',
                                        widget=forms.FileInput(attrs={
                                            'accept': '.tsv',
                                        })
                                        )

    class Meta:
        model = Sequence
        fields = ('Primers',)


#primers
class PrimersCreateEditForm(forms.ModelForm):
    class Meta:
        model = Primers
        fields = ('Query',
                  "Forword_Primer",
                  "Reverse_Primer",
                  "Created_at")




class BookCreateEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author',
                  'title',
                  'description',
                  'quantity', 
                  'category',
                  'publisher',
                  'floor_number',
                  "bookshelf_number")


class PubCreateEditForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name',
                  'city',
                  'contact',
                  )
        # fields="__all__"


class MemberCreateEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name',
                  'gender',
                  'age',
                  'email',
                  'city', 
                  'phone_number',)


class ProfileForm(forms.ModelForm):

    
    class Meta:
        model = Profile
        fields = ( 'profile_pic',
                  'bio', 
                  'phone_number',
                  'email')


class BorrowRecordCreateForm(forms.ModelForm):

    borrower = forms.CharField(label='Borrrower', 
                    widget=forms.TextInput(attrs={'placeholder': 'Search Member...'}))
    
    book = forms.CharField(help_text='type book name')

    class Meta:
        model = BorrowRecord
        fields=['borrower','book','quantity','start_day','end_day']
        # widgets = {
        #     'start_day': DatePickerInput().start_of('event datetime'),
        #     'end_day': DatePickerInput().end_of('event datetime'),
        # }
        widgets = {
            'start_day': DatePickerInput(options = {  "dateFormat": "Y-m-d", }),
            'end_day': DatePickerInput(options = {  "dateFormat": "Y-m-d", }),
        }

