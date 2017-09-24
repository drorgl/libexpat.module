{
    'variables': {
        #'library': 'static_library',
        'library' : 'shared_library',
    },
    #gen_test_char!!!
    "targets": [
        {
            'target_name': 'libexpat',
            'type': '<(library)',
            'dependencies': [
            ],
            'include_dirs':[
                "src/expat/lib",
            ],
            "defines":[
                'HAVE_GETRANDOM'
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                   "src/expat/lib",
                ],
                "defines":[
                ],
            },
            'conditions':[
				['OS != "win"',{
					'sources':[
                        "src/expat/xmlwf/unixfilemap.c",
					],
					'link_settings':{
						'libraries':[
						],
					},
				}],
				['OS == "win"',{
                    'sources':[
                        "src/expat/xmlwf/win32filemap.c",
                    ],
					'link_settings': {
						'libraries': [
						]
					}
				}]
				
			],
            'sources':[
                "build_windows.bat",
                "libexpat.gyp",
                "src/expat/AUTHORS",
                "src/expat/conftools/ac_c_bigendian_cross.m4",
                "src/expat/conftools/expat.m4",
                "src/expat/conftools/get-version.sh",
                "src/expat/conftools/PrintPath",
                "src/expat/COPYING",
                "src/expat/doc/doc.mk",
                "src/expat/doc/expat.png",
                "src/expat/doc/Makefile.am",
                "src/expat/doc/reference.html",
                "src/expat/doc/style.css",
                "src/expat/doc/valid-xhtml10.png",
                "src/expat/doc/xmlwf.xml",
                #"src/expat/gennmtab/gennmtab.c",
                "src/expat/lib/ascii.h",
                "src/expat/lib/asciitab.h",
                "src/expat/lib/expat.h",
                "src/expat/lib/expat_external.h",
                "src/expat/lib/iasciitab.h",
                "src/expat/lib/internal.h",
                "src/expat/lib/latin1tab.h",
                "src/expat/lib/libexpat.def",
                #"src/expat/lib/libexpatw.def",
                "src/expat/lib/loadlibrary.c",
                "src/expat/lib/nametab.h",
                "src/expat/lib/siphash.h",
                "src/expat/lib/utf8tab.h",
                "src/expat/lib/winconfig.h",
                "src/expat/lib/xmlparse.c",
                "src/expat/lib/xmlrole.c",
                "src/expat/lib/xmlrole.h",
                "src/expat/lib/xmltok.c",
                "src/expat/lib/xmltok.h",
                "src/expat/lib/xmltok_impl.c",
                "src/expat/lib/xmltok_impl.h",
                "src/expat/lib/xmltok_ns.c",
                #"src/expat/memory-sanitizer-blacklist.txt",
                "src/expat/README.md",

                "src/expat/win32/expat.iss",
                "src/expat/win32/MANIFEST.txt",
                "src/expat/win32/README.txt",

                #"src/expat/xmlwf/codepage.c",
                #"src/expat/xmlwf/codepage.h",
                ##"src/expat/xmlwf/ct.c",
                #"src/expat/xmlwf/filemap.h",
                #"src/expat/xmlwf/readfilemap.c",
                #
                #
                #"src/expat/xmlwf/xmlfile.c",
                #"src/expat/xmlwf/xmlfile.h",
                #"src/expat/xmlwf/xmlmime.c",
                #"src/expat/xmlwf/xmlmime.h",
                #"src/expat/xmlwf/xmltchar.h",
                #"src/expat/xmlwf/xmlurl.h",
                #"src/expat/xmlwf/xmlwf.c",
                ##"src/expat/xmlwf/xmlwin32url.cxx",
                "src/README.md",


            ]
        },
        {
            'target_name': 'elements',
            'type': 'executable',
            'dependencies': [
                'libexpat'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/expat/examples/elements.c",
            ]
        },
        {
            'target_name': 'outline',
            'type': 'executable',
            'dependencies': [
                'libexpat'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/expat/examples/outline.c",
            ]
        },
        {
            'target_name': 'benchmark',
            'type': 'executable',
            'dependencies': [
                'libexpat'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/expat/tests/benchmark/benchmark.c",
                "src/expat/tests/benchmark/README.txt",
            ]
        },
        {
            'target_name': 'expat-tests',
            'type': 'static_library',
            'dependencies': [
                'libexpat'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                 "src/expat/tests/minicheck.c",
                "src/expat/tests/minicheck.h",

                "src/expat/tests/chardata.c",
                "src/expat/tests/chardata.h",

                "src/expat/tests/structdata.c",
                "src/expat/tests/structdata.h",

                "src/expat/tests/memcheck.c",
                "src/expat/tests/memcheck.h",
                
                #"src/expat/tests/README.txt",
            ]
        },
         {
            'target_name': 'runtests',
            'type': 'executable',
            'dependencies': [
                'libexpat',
                'expat-tests'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/expat/tests/runtests.c",
            ]
        },
        {
            'target_name': 'runtestspp',
            'type': 'executable',
            'dependencies': [
                'libexpat',
                'expat-tests'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/expat/tests/runtestspp.cpp",

               
                
                #"src/testdata/largefiles/nes96.xml",
                #"src/testdata/largefiles/ns_att_test.xml",
                #"src/testdata/largefiles/README.txt",
                #"src/testdata/largefiles/recset.xml",
                #"src/testdata/largefiles/wordnet_glossary-20010201.rdf",
                #"src/testdata/README.txt",

            ]
        }
    ]
}
