import { 
  Card,
  CardHeader, 
  CardContent, 
  IconButton,
  Box,
} from "@mui/material"
  
import { DataGrid } from '@mui/x-data-grid'
import EditIcon from '@mui/icons-material/Edit'
  
  
const ProjectsCard = ({ user }) => {
  return (
    <div>
      <Card>
        <CardHeader
          action={
            <IconButton>
              <EditIcon />
            </IconButton>
          }
          title="Projects"
          />
        <CardContent> 
        
        </CardContent>
      </Card>
    </div>
  )
}

export default ProjectsCard