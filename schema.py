schema = [
    {
        "name": "shelter",
        "description": "Shelter and basic needs",
        "title": "Shelter",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Shelter Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "weekdayHours",
                "title": "Weekday Opening Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {"name": "day", "type": "string"},
                            {"name": "hours", "type": "string"},
                            {"name": "requiresAppointment", "type": "boolean"},
                        ],
                    }
                ],
            },
            {
                "name": "weekendHours",
                "title": "Weekend Opening Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {"name": "day", "type": "string"},
                            {"name": "hours", "type": "string"},
                            {"name": "requiresAppointment", "type": "boolean"},
                        ],
                    }
                ],
            },
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "type": "string"},
                    {"name": "hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {"name": "type", "type": "string"},
                            {"name": "number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "type": "string"},
                    {"name": "postalCode", "type": "string"},
                    {"name": "city", "type": "string"},
                    {"name": "googleMapsLink", "type": "url"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
            {
                "name": "shelterType",
                "title": "Shelter Type",
                "type": "string",
                "options": {
                    "list": [
                        {"title": "Day Shelter", "value": "day"},
                        {"title": "Night Shelter", "value": "night"},
                    ]
                },
            },
        ],
    },
    {
        "name": "dentist",
        "title": "Dentist",
        "description": "Dentist and dental care",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Dentist Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "foodAndClothing",
        "title": "Food and Clothing",
        "description": "Food and clothing distribution",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Organization Name", "type": "string"},
            {
                "name": "description",
                "title": "Description",
                "type": "markdown",
                "description": "Provide details about the meal, special notes, or additional information.",
            },
            {
                "name": "openingHours",
                "title": "Opening Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "days",
                                "title": "Days",
                                "type": "string",
                                "description": "Specify days (e.g., Saturdays, Weekends).",
                            },
                            {
                                "name": "hours",
                                "title": "Hours",
                                "type": "string",
                                "description": "Specify time range (e.g., 10:30-15:00).",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., General, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "website",
                "title": "Website",
                "type": "url",
                "description": "Link to the service’s website or additional information.",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Available Hours", "type": "string"},
                ],
            },
            {
                "name": "needToKnow",
                "title": "What You Need to Know",
                "type": "markdown",
                "description": "Provide important details, like documents required or rules to follow.",
            },
            {
                "name": "foodOrClothing",
                "title": "Food or Clothing",
                "type": "string",
                "options": {
                    "list": [
                        {"title": "Food", "value": "food"},
                        {"title": "Clothing", "value": "clothing"},
                    ]
                },
            },
        ],
    },
    {
        "name": "legal",
        "title": "Legal",
        "description": "Legal advice and support. This includes legal advice, legal representation, and legal aid.",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Legal Advice Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                    {
                        "name": "googleMapsLink",
                        "title": "Google Maps Link",
                        "type": "url",
                    },
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "healthAndWellbeing",
        "title": "Healthcare Documentation",
        "description": "Healthcare documentation. This includes healthcare documentation, healthcare services, and healthcare support.",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "emergencyLines",
        "title": "Emergency Lines",
        "description": "Emergency lines. This includes emergency services, police, and emergency support.",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "doctors",
        "title": "Doctors",
        "description": "Doctors. This includes doctors, healthcare services, and healthcare support.",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "medication",
        "title": "Medication",
        "description": "Medication. This includes medication, healthcare services, and healthcare support.",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "sexualHealth",
        "title": "Sexual Health",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "mentalWellbeing",
        "title": "Mental Wellbeing",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "hygiene",
        "title": "Hygiene",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "emergencyPolice",
        "title": "Emergency Services & Police",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "domesticViolence",
        "title": "Domestic Violence",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "criminalExploitation",
        "title": "Criminal Exploitation",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "sexualExploitation",
        "title": "Sexual Exploitation",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "labourExploitation",
        "title": "Labour Exploitation",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Service Name", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "emergencyContact",
                "title": "Emergency Contact",
                "type": "object",
                "fields": [
                    {"name": "phone", "title": "Phone", "type": "string"},
                    {"name": "hours", "title": "Hours", "type": "string"},
                ],
            },
            {"name": "website", "title": "Website", "type": "url"},
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "phoneNumbers",
                "title": "Phone Numbers",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "type",
                                "title": "Type",
                                "type": "string",
                                "description": "E.g., Reception, Emergency",
                            },
                            {"name": "number", "title": "Number", "type": "string"},
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
    {
        "name": "work",
        "title": "Work",
        "description": "Work. This includes work, employment, and employment support. Also includes labour rights information and flyers",
        "type": "document",
        "fields": [
            {"name": "name", "title": "Labour Rights Information", "type": "string"},
            {"name": "description", "title": "Description", "type": "markdown"},
            {
                "name": "operatingHours",
                "title": "Operating Hours",
                "type": "array",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "label",
                                "title": "Label",
                                "type": "string",
                                "description": "Specify the time range (e.g., Monday-Friday, Weekends, Holidays)",
                            },
                            {"name": "hours", "title": "Hours", "type": "string"},
                            {
                                "name": "requiresAppointment",
                                "title": "Requires Appointment",
                                "type": "boolean",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "needToKnow",
                "title": "What do you need to know?",
                "type": "markdown",
            },
            {"name": "website", "title": "Website", "type": "url"},
            {"name": "email", "title": "Email", "type": "string"},
            {
                "name": "flyers",
                "title": "Flyers",
                "type": "array",
                "description": "Flyers in different languages. This contains more information about work rights and labour rights.",
                "of": [
                    {
                        "type": "object",
                        "fields": [
                            {
                                "name": "language",
                                "title": "Flyer Language",
                                "type": "string",
                                "description": "Specify the language of the flyer (e.g., English, Spanish).",
                            },
                            {
                                "name": "link",
                                "title": "Flyer PDF Link",
                                "type": "url",
                                "description": "Link to the PDF version of the flyer.",
                            },
                        ],
                    }
                ],
            },
            {
                "name": "address",
                "title": "Address",
                "type": "object",
                "fields": [
                    {"name": "street", "title": "Street", "type": "string"},
                    {"name": "postalCode", "title": "Postal Code", "type": "string"},
                    {"name": "city", "title": "City", "type": "string"},
                ],
            },
            {"name": "logo", "title": "Logo", "type": "image"},
        ],
    },
]
