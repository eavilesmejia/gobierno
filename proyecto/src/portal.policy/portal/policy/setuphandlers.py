from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException




#lista para excluir de la navegacion
excluir_nav=['actualidad','agenda','faq','ayuda','glosario','imagenes','video','galeria']

def deletePloneFolders(p):
    """Eliminar el contenido existente"""
    #Eliminar folders estandard
    existing = p.objectIds()
    itemsToDelete = ['news', 'events','Members','front-page']
    for item in itemsToDelete:
        if item in existing:
            p.manage_delObjects(item)

def createFolderStructure(site):
    """Definir los objetos que quiero crear"""

    actualidad_children = [
    {'id':'eventos',
     'title':'Eventos',
     'description': '',
     'type':'Folder',
     'layout':'icons_description',
    },
    {'id': 'comunicados',
     'title': 'Comunicados',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    {'id': 'avisos',
     'title': 'Avisos',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    ]

    aoi_children = [
    {'id':'objetivo',
     'title':'Objetivos',
     'description': '',
     'type':'Document',
     'layout':'Common',
    },
    {'id': 'asistencia',
     'title': 'Asistencia Ofrecida',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'contacto',
     'title': 'Contacto',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'formulario-solicitud',
     'title': 'Formularios de Solicitud de Informacion',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'informes',
     'title': 'Informes',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'boletin',
     'title': 'Boletin',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_listing',
    },
    {'id': 'estadistica',
     'title': 'Estadistica',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    ]

    qs_children = [
    {'id':'base-legal',
     'title':'Base Legal',
     'description': '',
     'type':'Document',
     'layout':'Common',
    },
    {'id': 'mision-y-vision',
     'title': 'Mision y Vision',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'plan-estrategico',
     'title': 'Plan Estrategico',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'politica-institucional',
     'title': 'Politica Institucional',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'valores',
     'title': 'Valores',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'funciones',
     'title': 'Funciones',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'donde-estamos',
     'title': 'Donde Estamos',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    ]

    ministro_children = [
    {'id': 'discursos',
     'title': 'Discursos',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    {'id': 'presentaciones',
     'title': 'Presentaciones',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    {'id': 'escritos',
     'title': 'Escritos',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    ]

    documentos_children = [
    {'id':'normas',
     'title':'Normas',
     'description': '',
     'type':'Folder',
     'layout':'folder_tabular_view',
    },
    {'id': 'leyes',
     'title': 'Leyes',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'procedimientos',
     'title': 'Procedimientos',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'manuales',
     'title': 'Manuales',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'acuerdos-ministeriales',
     'title': 'Acuerdos Ministeriales',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'circulares',
     'title': 'Circulares',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'publicaciones',
     'title': 'Publicaciones',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'encuestas',
     'title': 'Encuestas',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    {'id': 'otros',
     'title': 'Otros',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_tabular_view',
    },
    ]

    direccion_children = [
    {'id':'base-legal',
     'title':'Base Legal',
     'description': '',
     'type':'Document',
     'layout':'Common',
    },
    {'id': 'mision-y-vision',
     'title': 'Mision y Vision',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'estructura-organizativa',
     'title': 'Estructura Organizativa',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'servicios',
     'title': 'Servicios',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'documentos',
     'title': 'Documentos',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'funciones',
     'title': 'Funciones',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    {'id': 'preguntas-frecuentes',
     'title': 'Preguntas Frecuentes',
     'description': '',
     'type': 'Document',
     'layout': 'Common',
    },
    ]

    direcSup_children = [
    {'id': 'ministro',
     'title': 'Ministro',
     'description': 'Discursos, Presentaciones, Escritos',
     'type': 'Folder',
     'layout': 'icons_description',
     'children':ministro_children,
    },
    {'id': 'viceministro',
     'title': 'Vice Ministro',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    {'id': 'secretario-general',
     'title': 'Secretario General',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    ]

    noticias_children = [
    {'id':'noticia-1',
     'title':'Noticia 1',
     'description': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis.',
     'type':'News Item',
     'layout':'newsitem_view',
    },
    {'id':'noticia-2',
     'title':'Noticia 2',
     'description': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis.',
     'type':'News Item',
     'layout':'newsitem_view',
    },
    ]
    
    institucion_children = [
    {'id':'qs',
     'title':'Quienes Somos',
     'description': 'Base legal, Mision, Vision, Plan estrategico, Politica Institucional, valores, Funciones, Donde Estamos',
     'type':'Folder',
     'layout':'icons_description',
     'children':qs_children,
    },
    {'id': 'direccion-superior',
     'title': 'Direccion Superior',
     'description': 'Ministro, ViceMinistro, Secretario General',
     'type': 'Folder',
     'layout': 'icons_description',
     'children':direcSup_children,
    },
    {'id': 'organigrama',
     'title': 'Organigrama',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    {'id': 'directorio',
     'title': 'Directorio Institucional',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    {'id': 'poa',
     'title': 'Plan Anual Operativo',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
    },
    ]

    direccionx = [
    {'id':'direccionx',
     'title':'Direccion x',
     'description': 'Base Legal, Mision y Vision, Estructura Organizativa, Funciones, Servicios, Documentos, Preguntas Frecuentes',
     'type':'Folder',
     'layout':'icons_description',
     'children':direccion_children
    },
    ]
    
    top_folders = [
    {'id': 'actualidad',
     'title': 'Actualidad',
     'description': 'Eventos, Comunicados, Avisos',
     'type': 'Folder',
     'layout': 'icons_description',
     'children': actualidad_children,
    },
    {'id': 'agenda',
     'title': 'Agenda',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
     },
    {'id': 'galeria',
     'title': 'Galeria de Fotos',
     'description': 'Glarias de Foto',
     'type': 'Folder',
     'layout': 'atct_album_view',
     },
    {'id': 'video',
     'title': 'VideoTeca',
     'description': 'Conferencias, talleres',
     'type': 'Folder',
     'layout': 'folder_listing',
     },
     {'id': 'faq',
     'title': 'Preguntas Frecuentes',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_listing',
     },
     {'id': 'ayuda',
     'title': 'Ayuda del sitio',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_listing',
     },
     {'id': 'glosario',
     'title': 'Glosario',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_listing',
     },
     {'id': 'institucion',
     'title': 'La Institucion',
     'description': 'Quines somos, Direccion Superior, Organigrama, Directorio, Plan Anual Operativo',
     'type': 'Folder',
     'layout': 'icons_description',
     'children':institucion_children,
     },
     {'id': 'servicios',
     'title': 'Servicios',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
     },
     {'id': 'direcciones-generales',
     'title': 'Direcciones Generales',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
     'children':direccionx,
     },
     {'id': 'programas-y-proyectos',
     'title': 'Programas y Proyectos',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
     },
     {'id': 'oai',
     'title': 'Oficina de Acceso a la Informacion',
     'description': 'Objetivo, Asistencia Ofrecida, Contacto, Formularios de Solicitud de Informacion, Informes, Boletin, Estadistica',
     'type': 'Folder',
     'layout': 'icons_description',
     'children':aoi_children,
     },
     {'id': 'documentos',
     'title': 'Documentos',
     'description': 'Normas, Leyes, Procedimientos, Manuales, Acuerdo Ministeriales, Circulares, Publicaciones, Encuestas, Otros',
     'type': 'Folder',
     'layout': 'document_view',
     'children':documentos_children,
     },
     {'id': 'arte-y-cultura',
     'title': 'Arte y Cultura',
     'description': '',
     'type': 'Folder',
     'layout': 'icons_description',
     },
     {'id': 'noticias',
     'title': 'Noticias',
     'description': '',
     'type': 'Folder',
     'layout': 'folder_summary_view',
     'children':noticias_children,
     },
     {'id': 'imagenes',
      'title': 'Imagenes',
      'description':'imangenes del portal',
      'type':'Folder',
      'layout':'folder_tabular_view',
     },
     {'id': 'ultimos-documentos',
      'title': 'ultimos Documentos',
      'description':'Ultimos Documentos del Portal',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'proximos-eventos',
      'title': 'Proximos Eventos',
      'description':'Proximos Eventos del portal',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'estudiantes-docentes',
      'title': 'Estudiantes y Docentes',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'ciudadano',
      'title': 'Ciudadano',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'instituciones',
      'title': 'Instituciones',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'proveedores',
      'title': 'Proveedores del Estado',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'ong',
      'title': 'ONG',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'profesionales',
      'title': 'Profesionales',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     {'id': 'empresa',
      'title': 'Empresa Privada',
      'description':'',
      'type':'Topic',
      'layout':'atct_topic_view',
     },
     ]
    createObjects(site,top_folders)
    objectCollection(site,top_folders[-9:])

#Modulo para crear los objetos
def createObjects(parent, children):
    """este deberia crear nuevos objetos, excluir de navegacion
    algunos y plublicar todo el contenido.
    """

    #variable que contiene el workflow de plone
    wtool = getToolByName(parent,'portal_workflow')

    parent.plone_log("Creating %s in %s" % (children, parent))
    existing = parent.objectIds()
    parent.plone_log("Existing ids: %s" % existing)

    for new_object in children:
        if new_object['id'] in existing:
            parent.plone_log("%s exists, skipping" % new_object['id'])
        else:
            #crear objeto
            if new_object['id'] in ('noticia-1','noticia-2'):
                parent.invokeFactory(id=new_object['id'],
                      type_name=new_object['type'],
                      title=new_object['title'],
                      description=new_object['description'],
                      text='<p>at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum.</p>',
                      subject=["estudiante","ciudadano","instituciones","proveedores","ong","profesionales","empresa privada"])
            else:
                parent.invokeFactory(id=new_object['id'],
                      type_name=new_object['type'],
                      title=new_object['title'],
                      description=new_object['description'])

            #Publicar Objeto
            objeto=getattr(parent,new_object['id'])
            objeto.indexObject()
            try:
                if wtool.getInfoFor(objeto,'review_state') != 'published':
                    wtool.doActionFor(objeto,'publish',comment='Publicando objeto...')
                    parent.plone_log('se ha publicado el contenido %s' %objeto)
            except WorkflowException:
                parent.plone_log('no se ha publicado el contenido')

            #Cambiar permiso al objeto
            objeto.manage_permission('View', roles=['Manager', 'Owner'], acquire=True)
            #objeto.unmarkCreationFlag()
            #Excluir de Navegacion
            for excluir in excluir_nav:
                if excluir==new_object['id'] or new_object['type']!='Folder':
                    objeto.setExcludeFromNav(True)
                    objeto.reindexObject()
                    parent.plone_log('se ha excluido de la navegacion %s' %objeto)
            parent.plone_log("Ahora ha modificado new_object...")
#            obj = parent.get(new_object['id'], 0)
            if objeto is None:
                parent.plone_log("no se puede obtener new_object %s para modificarlo!" % new_object['id'])
            else:
                if objeto.Type() != new_object['type']:
                    parent.plone_log("Tipos no coinciden!")
                else:
                    #seleccionar el layout del objeto
                    objeto.setLayout(new_object['layout'])
                    objeto.reindexObject()
                    objeto.reindexObjectSecurity()
                    children = new_object.get('children',0)
                    if children>0:
                        createObjects(objeto,children)


def objectCollection(parent,children):
    """
     crea los criterio para la colleccion
     La colection tendra un limite de resultado 2
     con el criterio de Tipo de elmento con el valor noticia
     el tipo de ordenacion con la fecha efectiva invertida
     y la dejar la coleccion como pagina inicial
    """
    for objeto in children:
        theCollection = getattr(parent, objeto['id'])
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)

        #theCollection.setLayout('colection_view')
            
        if objeto['id']=='ultimos-documentos':
            theCriteria = theCollection.addCriterion('Type','ATPortalTypeCriterion')
            theCriteria.setValue("File")
            theCriteria=theCollection.addCriterion('modified','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='proximos-eventos':
            theCriteria = theCollection.addCriterion('Type','ATPortalTypeCriterion')
            theCriteria.setValue("Event")
            theCriteria = theCollection.addCriterion('start','ATSortCriterion')
            theCriteria.setReversed(False)
            
        if objeto['id']=='estudiantes-docentes':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("estudiante")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='ciudadano':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("ciudadano")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='instituciones':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("instituciones")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='proveedores':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("proveedores")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='ong':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("ong")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='profesionales':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("profesionales")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)
            
        if objeto['id']=='empresa':
            theCriteria = theCollection.addCriterion('Subject','ATSelectionCriterion')
            theCriteria.setValue("empresa privada")
            theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
            theCriteria.setReversed(True)

        theCollection.reindexObject()
#Modulo que se manda a llamar desde importstep.xml
def importVarious(context):
    if context.readDataFile('portal.policy_various.txt') is None:
        return
    site = context.getSite()
    deletePloneFolders(site)
    createFolderStructure(site)
