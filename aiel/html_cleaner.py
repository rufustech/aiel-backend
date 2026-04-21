"""
Utility to clean HTML content from TinyMCE editor artifacts
"""
import re


def clean_html_content(html_content):
    """
    Remove TinyMCE editor attributes from HTML content.
    Removes all data-* attributes that are added by the TinyMCE editor.
    
    Args:
        html_content (str): Raw HTML content from TinyMCE
        
    Returns:
        str: Cleaned HTML content without editor artifacts
    """
    if not html_content:
        return ""
    
    # Remove all data-* attributes (TinyMCE editor artifacts)
    # This regex matches: data-attribute-name="value" or data-attribute-name='value' or data-attribute-name=value
    # First pass: Remove data-* attributes with quoted values
    cleaned = re.sub(
        r'\s+data-[a-z-]+=["\'`][^\'">`]*["\'`]',
        '',
        html_content,
        flags=re.IGNORECASE
    )
    
    # Second pass: Remove any remaining data-* attributes without quotes
    cleaned = re.sub(
        r'\s+data-[a-z-]+=[^\s>]*',
        '',
        cleaned,
        flags=re.IGNORECASE
    )
    
    # Third pass: Remove any data-* attributes that span multiple lines or have escaped quotes
    cleaned = re.sub(
        r'\s+data-[a-z-]+[\s\n]*=[\s\n]*[^>]*?(?=[>\s])',
        '',
        cleaned,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    return cleaned
