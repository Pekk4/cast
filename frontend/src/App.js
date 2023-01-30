import { Container, Toolbar, AppBar, IconButton, Button } from "@mui/material"
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import React, { useState, useEffect } from "react"
import Notes from "./Components/Notes"
import NoteService from "./Services/NoteService"
import ConsultService from "./Services/ConsultService"
import Home from "./Components/Home"
import Profile from "./Components/Profile"
import Search from "./Components/Search"
import Login from "./Components/Login"

const App = () => {
  const [content, setContent] = useState([])
  const [consult, setConsult] = useState([])
  const [newContent, setNewContent] = useState("")

  const padding = {
    padding: 5,
  }

  useEffect(() => {
    NoteService.getAllNotes().then((initialNotes) => {
      setContent(initialNotes)
    })
  }, [])

  useEffect(() => {
    ConsultService.getAllConsults().then((consults) => {
      setConsult(consults)
    })
  }, [])

  const submitContent = (event) => {
    event.preventDefault()
    const contentObject = {
      content: newContent,
    }

    NoteService.createNote(contentObject)
      .then((returnedNote) => {
        setContent(content.concat(returnedNote))
        setNewContent("")
      })
      .catch((error) => {
        console.log(error)
      })
  }
  const handleContentChange = (event) => {
    setNewContent(event.target.value)
  }

  return (
    <Container>
      <Router>
        <div>
          <h1>Competency, Allocation and Skill tracker</h1>
        </div>
        <div>
          <AppBar>
            <Toolbar>
              <IconButton
                edge="start"
                color="inherit"
                aria-label="menu"
              ></IconButton>
              <Button color="inherit" component={Link} to="/" id="home">
                home
              </Button>
              <Button color="inherit" component={Link} to="/search" id="search">
                search
              </Button>
              <Button color="inherit" component={Link} to="/profile" id="profile">
                profile
              </Button>
              <Button color="inherit" component={Link} to="/notes" id="api">
                api
              </Button>
            </Toolbar>
          </AppBar>
        </div>
        <Routes>
          <Route
            path="/notes"
            element={
              <Notes
                notes={content}
                submitContent={submitContent}
                newContent={newContent}
                handleContentChange={handleContentChange}
              />
            }
          />
          <Route path="/search" element={<Search />} />
          <Route path="/profile" element={<Profile consult={consult} />} />
          <Route path="/" element={<Home />} />
        </Routes>
        <div>
          <i>Cast APP, OhTu-projekti 2023</i>
        </div>
      </Router>
    </Container>
  )
}

export default App
