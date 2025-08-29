import React, { useState } from 'react'
import '../css/HeaderGenerator.css'

function UserInfoForm({ onSubmit }) {
  const [form, setForm] = useState({
    name: '',
    location: '',
    email: '',
    phone: '',
    linkedin_link: '',
    linkedin_display: ''
  })

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (onSubmit) onSubmit(form)
  }

  return (
    <div className="user-info-form">
      <h2>Enter Basic Information</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" value={form.name} onChange={handleChange} />
        <input type="text" name="location" placeholder="Location" value={form.location} onChange={handleChange} />
        <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} />
        <input type="text" name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} />
        <input type="text" name="linkedin_link" placeholder="LinkedIn Link" value={form.linkedin_link} onChange={handleChange} />
        <input type="text" name="linkedin_display" placeholder="LinkedIn User Name" value={form.linkedin_display} onChange={handleChange} />
        <button type="submit" className="user-info-submit">Submit Info</button>
      </form>
    </div>
  )
}

export default UserInfoForm